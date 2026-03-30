from __future__ import annotations

import os
from pathlib import Path
import time
from typing import Iterable
import json
from datetime import datetime

from dotenv import load_dotenv

try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None


def load_model_env(provider: str) -> tuple[str, str, str, str]:
    # Load project root .env first, then assignment folder .env as fallback.
    load_dotenv(override=False)
    assignment_env = Path("作业要求") / ".env"
    if assignment_env.exists():
        load_dotenv(dotenv_path=assignment_env, override=False)

    provider = provider.lower()
    if provider == "gpt":
        key = os.getenv("OPENAI_API_KEY", "")
        # Compatible with tutorial style HOST_URL and OpenAI-style base_url.
        raw_base = os.getenv("OPENAI_BASE_URL", "") or os.getenv("HOST_URL", "") or os.getenv("GPT_HOST_URL", "")
        base = _normalize_base_url(raw_base)
        gen = os.getenv("OPENAI_GENERATOR_MODEL", "") or os.getenv("GENERATOR_MODEL", "gpt-5-nano")
        ref = os.getenv("OPENAI_REFINER_MODEL", "") or os.getenv("REFINER_MODEL", "gpt-5-mini")
        return key, base, gen, ref
    if provider == "ds":
        key = os.getenv("DEEPSEEK_API_KEY", "")
        base = _normalize_base_url(os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"))
        gen = os.getenv("DEEPSEEK_GENERATOR_MODEL", "") or os.getenv("GENERATOR_MODEL", "deepseek-chat")
        ref = os.getenv("DEEPSEEK_REFINER_MODEL", "") or os.getenv("REFINER_MODEL", "deepseek-chat")
        return key, base, gen, ref
    return "", "", "", ""


def _normalize_base_url(base: str) -> str:
    base = (base or "").strip()
    if not base:
        return ""
    if base.endswith("/"):
        base = base[:-1]
    if base.endswith("/v1"):
        return base
    return f"{base}/v1"


class LLMHeuristicClient:
    def __init__(
        self,
        api_key: str,
        base_url: str,
        generator_model: str,
        refiner_model: str,
        generator_provider: str | None = None,
        refiner_provider: str | None = None,
        generator_api_key: str | None = None,
        generator_base_url: str | None = None,
        refiner_api_key: str | None = None,
        refiner_base_url: str | None = None,
        verbose: bool = True,
    ) -> None:
        self.enabled = bool(api_key and OpenAI)
        self.generator_model = generator_model
        self.refiner_model = refiner_model
        self.verbose = verbose
        self.request_timeout_sec = float(os.getenv("LLM_REQUEST_TIMEOUT", "120"))
        self.max_retries = max(0, int(os.getenv("LLM_REQUEST_RETRIES", "2")))
        self.retry_backoff_sec = float(os.getenv("LLM_REQUEST_RETRY_BACKOFF", "3"))
        self.generator_provider = (generator_provider or "").lower() or None
        self.refiner_provider = (refiner_provider or "").lower() or None

        self._client = OpenAI(api_key=api_key, base_url=base_url or None, timeout=self.request_timeout_sec) if self.enabled else None
        self._generator_client = None
        self._refiner_client = None
        if OpenAI:
            gen_key = generator_api_key or api_key
            gen_base = generator_base_url if generator_base_url is not None else base_url
            ref_key = refiner_api_key or api_key
            ref_base = refiner_base_url if refiner_base_url is not None else base_url
            if gen_key:
                self._generator_client = OpenAI(api_key=gen_key, base_url=gen_base or None, timeout=self.request_timeout_sec)
            if ref_key:
                self._refiner_client = OpenAI(api_key=ref_key, base_url=ref_base or None, timeout=self.request_timeout_sec)
        self._checkpoint_dir: Path | None = None
        self._request_seq = 0
        self._request_context: dict = {}
        self._feedback_context: dict = {}

    def set_checkpoint_dir(self, checkpoint_dir: str | Path | None) -> None:
        if not checkpoint_dir:
            self._checkpoint_dir = None
            return
        p = Path(checkpoint_dir)
        p.mkdir(parents=True, exist_ok=True)
        self._checkpoint_dir = p

    def set_request_context(self, context: dict | None) -> None:
        self._request_context = dict(context or {})

    def set_feedback_context(self, feedback: dict | None) -> None:
        self._feedback_context = dict(feedback or {})

    def generate_candidates(self, n: int) -> list[str]:
        if not self.enabled:
            return []
        feedback_block = self._format_feedback_block()
        prompt = (
            "Generate arithmetic expressions for online bin packing scoring. "
            "Allowed variables: item, remaining, after, fill, mean_remaining, stdev_remaining, exact_fit. "
            "Allowed functions: abs, min, max, sqrt. "
            f"{feedback_block}"
            "Return one expression per line only."
        )
        out = self._ask(self.generator_model, prompt, request_type="generate")
        candidates = [ln.strip() for ln in out.splitlines() if ln.strip()]
        return candidates[:n]

    def refine_topk(self, best_expressions: Iterable[str], n: int) -> list[str]:
        if not self.enabled:
            return []
        base = "\n".join(best_expressions)
        feedback_block = self._format_feedback_block()
        prompt = (
            "Refine these scoring expressions for online bin packing to improve packing efficiency and diversity.\n"
            f"Seed expressions:\n{base}\n\n"
            f"{feedback_block}"
            "Return only new expressions, one per line."
        )
        out = self._ask(self.refiner_model, prompt, request_type="refine")
        candidates = [ln.strip() for ln in out.splitlines() if ln.strip()]
        return candidates[:n]

    def _format_feedback_block(self) -> str:
        if not self._feedback_context:
            return ""

        lines: list[str] = ["Use this evolutionary feedback from previous candidates:"]
        best_score = self._feedback_context.get("best_score")
        worst_score = self._feedback_context.get("worst_score")
        if best_score is not None and worst_score is not None:
            lines.append(f"- score range: best={best_score}, worst={worst_score} (lower is better)")

        dominant = self._feedback_context.get("dominant_behavior") or {}
        if dominant:
            lines.append(
                "- dominant behavior signature repeats too much: "
                f"{dominant.get('count', 0)}/{dominant.get('total', 0)}"
            )

        good_examples = self._feedback_context.get("good_examples") or []
        if good_examples:
            lines.append("- keep useful traits from these better expressions:")
            for expr in good_examples[:3]:
                lines.append(f"  {expr}")

        bad_examples = self._feedback_context.get("bad_examples") or []
        if bad_examples:
            lines.append("- avoid patterns from these weaker expressions:")
            for expr in bad_examples[:3]:
                lines.append(f"  {expr}")

        lines.append("- goal: propose behaviorally different strategies, not surface-level rewrites.")
        return "\n" + "\n".join(lines) + "\n\n"

    def _ask(self, model: str, prompt: str, request_type: str) -> str:
        routed_provider = self.generator_provider if request_type == "generate" else self.refiner_provider
        routed_client = self._generator_client if request_type == "generate" else self._refiner_client
        if routed_client is None:
            routed_client = self._client

        self._request_seq += 1
        req_id = self._request_seq
        start_iso = datetime.now().isoformat(timespec="seconds")
        self._append_checkpoint(
            {
                "event": "llm_request_start",
                "request_id": req_id,
                "request_type": request_type,
                "model": model,
                "provider": routed_provider,
                "prompt_chars": len(prompt),
                "started_at": start_iso,
                **self._request_context,
            }
        )
        if self.verbose:
            print(f"[llm] request model={model}", flush=True)
        t0 = time.time()
        resp = None
        last_exc: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                req_payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are an expert heuristic designer."},
                        {"role": "user", "content": prompt},
                    ],
                }
                # Some reasoning-focused models are stricter about temperature handling.
                if "reasoner" not in model.lower():
                    req_payload["temperature"] = 0.8
                resp = routed_client.chat.completions.create(
                    **req_payload,
                )
                break
            except Exception as exc:
                last_exc = exc
                final_attempt = attempt >= self.max_retries
                self._append_checkpoint(
                    {
                        "event": "llm_request_error" if final_attempt else "llm_request_retry",
                        "request_id": req_id,
                        "request_type": request_type,
                        "model": model,
                        "provider": routed_provider,
                        "attempt": attempt + 1,
                        "max_attempts": self.max_retries + 1,
                        "elapsed_sec": round(time.time() - t0, 3),
                        "finished_at": datetime.now().isoformat(timespec="seconds"),
                        "error": str(exc),
                        **self._request_context,
                    }
                )
                if final_attempt:
                    raise
                sleep_sec = self.retry_backoff_sec * (attempt + 1)
                if self.verbose:
                    print(
                        f"[llm] retry {attempt + 1}/{self.max_retries} model={model} after error: {exc}",
                        flush=True,
                    )
                time.sleep(sleep_sec)

        if resp is None:
            raise RuntimeError(f"LLM request failed without response: {last_exc}")
        if self.verbose:
            print(f"[llm] response model={model} elapsed={time.time() - t0:.2f}s", flush=True)
        content = resp.choices[0].message.content or ""
        self._append_checkpoint(
            {
                "event": "llm_request_done",
                "request_id": req_id,
                "request_type": request_type,
                "model": model,
                    "provider": routed_provider,
                "elapsed_sec": round(time.time() - t0, 3),
                "finished_at": datetime.now().isoformat(timespec="seconds"),
                "response_chars": len(content),
                **self._request_context,
            }
        )
        return content

    def _append_checkpoint(self, payload: dict) -> None:
        if not self._checkpoint_dir:
            return
        fp = self._checkpoint_dir / "requests.jsonl"
        with fp.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")

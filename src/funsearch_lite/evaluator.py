from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
from statistics import mean, pstdev

from .datasets import Instance


@dataclass(slots=True)
class InstanceEval:
    name: str
    capacity: float
    bins_used: int
    optimal_bins: int | None
    gap: float | None
    gap_ratio: float | None
    source: str | None = None


@dataclass(slots=True)
class EvalResult:
    avg_bins_used: float
    avg_gap: float | None
    avg_gap_ratio: float | None
    per_instance: list[InstanceEval]
    behavior_signature: str


def pack_instance(items: list[float], scorer, capacity: float = 1.0) -> tuple[int, list[int]]:
    bins_remaining: list[float] = []
    choices: list[int] = []

    for item in items:
        feasible_idx = [i for i, rem in enumerate(bins_remaining) if rem >= item]
        if not feasible_idx:
            bins_remaining.append(capacity - item)
            choices.append(-1)
            continue

        m = mean(bins_remaining) if bins_remaining else capacity
        s = pstdev(bins_remaining) if len(bins_remaining) > 1 else 0.0
        feasible_remaining = [bins_remaining[i] for i in feasible_idx]
        feasible_after = [rem - item for rem in feasible_remaining]

        order_rem = sorted(range(len(feasible_idx)), key=lambda j: feasible_remaining[j])
        order_after = sorted(range(len(feasible_idx)), key=lambda j: feasible_after[j])
        rem_rank_map = {order_rem[pos]: pos for pos in range(len(order_rem))}
        after_rank_map = {order_after[pos]: pos for pos in range(len(order_after))}
        denom = max(1, len(feasible_idx) - 1)

        best_i = feasible_idx[0]
        best_score = -math.inf

        for local_j, i in enumerate(feasible_idx):
            rem = bins_remaining[i]
            after = rem - item
            fill = 1.0 - rem / capacity
            features = {
                "item": item,
                "remaining": rem,
                "after": after,
                "fill": fill,
                "mean_remaining": m,
                "stdev_remaining": s,
                "exact_fit": 1.0 if abs(after) < 1e-12 else 0.0,
                "bin_rank": rem_rank_map[local_j] / denom,
                "slack_rank": after_rank_map[local_j] / denom,
                "global_tightness": item / max(1e-9, m),
            }
            sc = scorer(features)
            if sc > best_score:
                best_score = sc
                best_i = i

        bins_remaining[best_i] -= item
        choices.append(best_i)

    return len(bins_remaining), choices


def _sample_behavior_trace(choices: list[int], points: int) -> str:
    if not choices:
        return ""
    points = max(1, points)
    n = len(choices)
    if n <= points:
        return ",".join(str(v) for v in choices)

    if points == 1:
        return str(choices[-1])

    step = (n - 1) / float(points - 1)
    idxs = [int(round(i * step)) for i in range(points)]
    compact_idxs: list[int] = []
    for idx in idxs:
        if not compact_idxs or idx != compact_idxs[-1]:
            compact_idxs.append(idx)
    return ",".join(str(choices[i]) for i in compact_idxs)


def evaluate_candidate(
    instances: list[Instance],
    scorer,
    behavior_signature_points: int = 120,
) -> EvalResult:
    per_instance: list[InstanceEval] = []
    signature_parts: list[str] = []

    gap_sum = 0.0
    gap_ratio_sum = 0.0
    gap_count = 0

    for inst in instances:
        bins_used, choices = pack_instance(inst.items, scorer, capacity=inst.capacity)
        gap = None
        gap_ratio = None
        if inst.optimal_bins is not None and inst.optimal_bins > 0:
            gap = float(bins_used - inst.optimal_bins)
            gap_ratio = gap / float(inst.optimal_bins)
            gap_sum += gap
            gap_ratio_sum += gap_ratio
            gap_count += 1

        sampled = _sample_behavior_trace(choices, behavior_signature_points)
        label = inst.name if inst.source is None else f"{inst.source}:{inst.name}"
        signature_parts.append(f"{label}:{bins_used}:{sampled}")
        per_instance.append(
            InstanceEval(
                name=inst.name,
                capacity=inst.capacity,
                bins_used=bins_used,
                optimal_bins=inst.optimal_bins,
                gap=gap,
                gap_ratio=gap_ratio,
                source=inst.source,
            )
        )

    behavior = "|".join(signature_parts)
    behavior_hash = hashlib.sha256(behavior.encode("utf-8")).hexdigest()
    avg_bins = sum(pi.bins_used for pi in per_instance) / max(1, len(per_instance))
    avg_gap = gap_sum / gap_count if gap_count > 0 else None
    avg_gap_ratio = gap_ratio_sum / gap_count if gap_count > 0 else None
    return EvalResult(
        avg_bins_used=avg_bins,
        avg_gap=avg_gap,
        avg_gap_ratio=avg_gap_ratio,
        per_instance=per_instance,
        behavior_signature=behavior_hash,
    )

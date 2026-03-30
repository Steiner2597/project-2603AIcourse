from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DedupStats:
    expr_hit: int = 0
    behavior_hit: int = 0
    new_eval: int = 0


class FunctionalDeduplicator:
    def __init__(self) -> None:
        self._expr_seen: set[str] = set()
        self._behavior_to_score: dict[str, float] = {}
        self.stats = DedupStats()

    def check_expr(self, expr_hash: str) -> bool:
        if expr_hash in self._expr_seen:
            self.stats.expr_hit += 1
            return True
        self._expr_seen.add(expr_hash)
        return False

    def lookup_behavior(self, behavior_signature: str) -> float | None:
        if behavior_signature in self._behavior_to_score:
            self.stats.behavior_hit += 1
            return self._behavior_to_score[behavior_signature]
        return None

    def record_behavior(self, behavior_signature: str, score: float) -> None:
        self._behavior_to_score[behavior_signature] = score
        self.stats.new_eval += 1

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import random


@dataclass(slots=True)
class Instance:
    """Container for a single bin packing instance."""

    name: str
    capacity: float
    items: list[float]
    optimal_bins: int | None = None
    source: str | None = None  # Which file it came from (e.g., binpack1)


def generate_synthetic_instances(size: str, seed: int = 42) -> list[Instance]:
    rng = random.Random(seed)
    profile = {
        "small": (12, 50),
        "medium": (24, 100),
        "large": (40, 180),
    }
    count, n_items = profile.get(size, profile["small"])
    instances: list[Instance] = []
    for idx in range(count):
        items = [rng.uniform(0.05, 0.95) for _ in range(n_items)]
        rng.shuffle(items)
        instances.append(
            Instance(
                name=f"synthetic_{idx:02d}",
                capacity=1.0,
                items=items,
                optimal_bins=None,
                source="synthetic",
            )
        )
    return instances


def _parse_orlib_file(path: Path) -> list[Instance]:
    """Parse a single OR-Library binpacking file into structured instances."""

    tokens = [tok for tok in path.read_text(encoding="utf-8", errors="ignore").split() if tok]
    if not tokens:
        return []

    cursor = 0
    try:
        total_instances = int(tokens[cursor])
    except ValueError:
        return []
    cursor += 1

    instances: list[Instance] = []
    for _ in range(total_instances):
        if cursor + 3 >= len(tokens):
            break
        name = tokens[cursor]
        try:
            capacity = float(tokens[cursor + 1])
            n_items = int(tokens[cursor + 2])
            optimal = int(tokens[cursor + 3])
        except ValueError:
            break
        cursor += 4

        items: list[float] = []
        for _ in range(n_items):
            if cursor >= len(tokens):
                break
            try:
                items.append(float(tokens[cursor]))
            except ValueError:
                pass
            cursor += 1

        if len(items) != n_items:
            # Malformed instance; stop parsing further to avoid silent drift.
            break

        instances.append(Instance(name=name, capacity=capacity, items=items, optimal_bins=optimal, source=path.stem))

    return instances


def list_orlib_sources(data_dir: str | Path) -> list[str]:
    root = Path(data_dir)
    if not root.exists():
        return []
    return [p.stem for p in sorted(root.glob("binpack*.txt"))]


def load_orlib_instances(data_dir: str | Path, source: str | None = None) -> list[Instance]:
    root = Path(data_dir)
    if not root.exists():
        return []

    instances: list[Instance] = []
    if source:
        target = source if source.endswith(".txt") else f"{source}.txt"
        files = [root / target]
    else:
        files = sorted(root.glob("binpack*.txt"))

    for txt in files:
        if not txt.exists():
            continue
        instances.extend(_parse_orlib_file(txt))
    return instances

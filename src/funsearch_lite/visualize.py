from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def save_curve(best: list[float], avg: list[float], output: str | Path) -> None:
    p = Path(output)
    p.parent.mkdir(parents=True, exist_ok=True)

    ratio_mode = bool(best and avg and max(best + avg) <= 1.0)
    plot_best = [v * 100.0 for v in best] if ratio_mode else best
    plot_avg = [v * 100.0 for v in avg] if ratio_mode else avg
    generations = list(range(1, len(plot_best) + 1))

    plt.figure(figsize=(8, 4.5))
    plt.plot(generations, plot_best, label="Best gap ratio (%)" if ratio_mode else "Best score", linewidth=2.0)
    plt.plot(generations, plot_avg, label="Avg gap ratio (%)" if ratio_mode else "Avg score", linewidth=1.8)
    plt.xlabel("Generation")
    plt.ylabel("Gap ratio to optimum (%; lower is better)" if ratio_mode else "Score (lower is better)")
    plt.title("FunSearch-Lite Evolution Trajectory (gap ratio %)" if ratio_mode else "FunSearch-Lite Evolution Trajectory")
    if generations:
        plt.xticks(generations)
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(p, dpi=140)
    plt.close()

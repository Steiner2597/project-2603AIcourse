from __future__ import annotations

import ast
import hashlib
import math
import random
import re


ALLOWED_NAMES = {
    "item",
    "remaining",
    "after",
    "fill",
    "mean_remaining",
    "stdev_remaining",
    "exact_fit",
    "bin_rank",
    "slack_rank",
    "global_tightness",
}

ALLOWED_FUNCS = {
    "abs": abs,
    "min": min,
    "max": max,
    "sqrt": math.sqrt,
}

BASE_EXPRESSIONS = [
    "-after",
    "exact_fit * 2.0 - after",
    "-(after * after)",
    "fill - after",
    "exact_fit + fill - 0.5 * after",
    "-abs(after - mean_remaining)",
    "-abs(after) + 0.3 * fill",
    "-after + 0.2 * exact_fit - 0.1 * stdev_remaining",
    "-after - 0.6 * slack_rank",
    "-after + 0.4 * (1.0 - bin_rank)",
    "-after - 0.2 * global_tightness + 0.3 * exact_fit",
]


class UnsafeExpressionError(ValueError):
    pass


def normalize_expression(expr: str) -> str:
    tree = ast.parse(expr, mode="eval")
    _validate_ast(tree)
    normalized = ast.unparse(tree)
    return normalized


def expression_hash(expr: str) -> str:
    norm = normalize_expression(expr)
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def build_scorer(expr: str):
    norm = normalize_expression(expr)
    code = compile(ast.parse(norm, mode="eval"), "<heuristic_expr>", "eval")

    def score_fn(features: dict[str, float]) -> float:
        local_env = {k: float(features.get(k, 0.0)) for k in ALLOWED_NAMES}
        value = eval(code, {"__builtins__": {}, **ALLOWED_FUNCS}, local_env)
        try:
            return float(value)
        except Exception as exc:  # pragma: no cover
            raise ValueError(f"Invalid score output: {value!r}") from exc

    return score_fn


def random_expression(rng: random.Random) -> str:
    if rng.random() < 0.35:
        return rng.choice(BASE_EXPRESSIONS)

    vars_pool = [
        "item",
        "remaining",
        "after",
        "fill",
        "mean_remaining",
        "stdev_remaining",
        "exact_fit",
        "bin_rank",
        "slack_rank",
        "global_tightness",
    ]
    k = rng.randint(3, 6)
    terms: list[str] = []
    for _ in range(k):
        coef = round(rng.uniform(-2.5, 2.5), 3)
        var = rng.choice(vars_pool)
        terms.append(f"({coef} * {var})")
    expr = " + ".join(terms)
    if rng.random() < 0.4:
        expr = f"({expr}) - abs(after)"
    if rng.random() < 0.3:
        expr = f"max(({expr}), -after)"
    return normalize_expression(expr)


def mutate_expression(expr: str, rng: random.Random) -> str:
    tokens = [
        "item",
        "remaining",
        "after",
        "fill",
        "mean_remaining",
        "stdev_remaining",
        "exact_fit",
        "bin_rank",
        "slack_rank",
        "global_tightness",
        "0.1",
        "0.2",
        "0.5",
        "1.0",
        "2.0",
        "+",
        "-",
        "*",
        "/",
    ]
    expr = normalize_expression(expr)
    if rng.random() < 0.45:
        term = rng.choice(tokens[:7])
        coef = rng.choice(["0.1", "0.2", "0.5", "1.0", "2.0"])
        op = rng.choice(["+", "-"])
        candidate = f"({expr}) {op} ({coef} * {term})"
    elif rng.random() < 0.75:
        candidate = f"-abs({expr})"
    else:
        candidate = f"max(({expr}), -abs(after))"
    return normalize_expression(candidate)


def crossover_expression(a: str, b: str, rng: random.Random) -> str:
    a = normalize_expression(a)
    b = normalize_expression(b)
    if rng.random() < 0.5:
        candidate = f"0.5 * ({a}) + 0.5 * ({b})"
    else:
        candidate = f"max(({a}), ({b}))"
    return normalize_expression(candidate)


def local_perturb_expression(expr: str, rng: random.Random) -> str:
    """Small local structural perturbation for post-search refinement."""
    expr = normalize_expression(expr)

    # 1) Slightly perturb one numeric constant if present.
    float_re = re.compile(r"(?<![A-Za-z_])[-+]?\d+\.\d+(?![A-Za-z_])")
    matches = list(float_re.finditer(expr))
    if matches and rng.random() < 0.65:
        m = rng.choice(matches)
        old_val = float(m.group(0))
        scale = rng.uniform(0.85, 1.15)
        new_val = round(old_val * scale, 4)
        candidate = expr[: m.start()] + str(new_val) + expr[m.end() :]
        return normalize_expression(candidate)

    # 2) Append a tiny correction term around new features.
    feature = rng.choice(["slack_rank", "bin_rank", "global_tightness", "after", "exact_fit"])
    coef = round(rng.uniform(-0.25, 0.25), 4)
    op = "+" if coef >= 0 else "-"
    candidate = f"({expr}) {op} ({abs(coef)} * {feature})"
    return normalize_expression(candidate)


def _validate_ast(tree: ast.AST) -> None:
    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Call,
        ast.Name,
        ast.Load,
        ast.Constant,
        ast.IfExp,
        ast.Compare,
        ast.Gt,
        ast.GtE,
        ast.Lt,
        ast.LtE,
        ast.Eq,
        ast.NotEq,
    )
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise UnsafeExpressionError(f"Disallowed AST node: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id not in ALLOWED_NAMES and node.id not in ALLOWED_FUNCS:
            raise UnsafeExpressionError(f"Disallowed identifier: {node.id}")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in ALLOWED_FUNCS:
                raise UnsafeExpressionError("Only abs/min/max/sqrt calls are allowed")

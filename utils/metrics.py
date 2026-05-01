from __future__ import annotations

import pandas as pd


def brier_score(probabilities: pd.Series, outcome: int) -> float:
    return float(((probabilities - outcome) ** 2).mean())


def time_to_threshold(probabilities: pd.DataFrame, threshold: float = 0.7) -> pd.Timestamp | None:
    hits = probabilities[probabilities["probability"] >= threshold]
    if hits.empty:
        return None
    return hits.iloc[0]["date"]


def probability_volatility(probabilities: pd.Series) -> float:
    moves = probabilities.diff().abs().dropna()
    if moves.empty:
        return 0.0
    return float(moves.mean())

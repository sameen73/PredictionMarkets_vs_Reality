from __future__ import annotations

import pandas as pd


MARKETS = pd.DataFrame(
    [
        {
            "market_id": "gas_2024_spike",
            "topic": "gas_prices",
            "label": "US gas above $3.80",
            "question": "Will the US national average gas price exceed $3.80 before Oct. 1, 2024?",
            "outcome": 0,
            "threshold": 3.80,
        },
        {
            "market_id": "gas_2024_summer",
            "topic": "gas_prices",
            "label": "US gas above $3.60",
            "question": "Will the US national average gas price exceed $3.60 during summer 2024?",
            "outcome": 1,
            "threshold": 3.60,
        },
        {
            "market_id": "conflict_red_sea",
            "topic": "conflict",
            "label": "Red Sea disruption persists",
            "question": "Will major Red Sea shipping disruptions continue through March 2024?",
            "outcome": 1,
            "threshold": None,
        },
        {
            "market_id": "conflict_ceasefire",
            "topic": "conflict",
            "label": "Ceasefire before June",
            "question": "Will a durable ceasefire be announced before June 1, 2024?",
            "outcome": 0,
            "threshold": None,
        },
        {
            "market_id": "election_senate",
            "topic": "elections",
            "label": "Modeled Senate seat flips",
            "question": "Will the challenger party win the modeled Senate seat in 2024?",
            "outcome": 1,
            "threshold": None,
        },
        {
            "market_id": "election_turnout",
            "topic": "elections",
            "label": "Turnout above 2020",
            "question": "Will modeled national turnout exceed the prior presidential cycle?",
            "outcome": 0,
            "threshold": None,
        },
    ]
)


PROBABILITIES = pd.DataFrame(
    [
        ("gas_2024_spike", "2024-04-01", 0.52),
        ("gas_2024_spike", "2024-05-01", 0.49),
        ("gas_2024_spike", "2024-06-01", 0.44),
        ("gas_2024_spike", "2024-07-01", 0.36),
        ("gas_2024_spike", "2024-08-01", 0.27),
        ("gas_2024_spike", "2024-09-01", 0.18),
        ("gas_2024_summer", "2024-04-01", 0.41),
        ("gas_2024_summer", "2024-05-01", 0.56),
        ("gas_2024_summer", "2024-06-01", 0.68),
        ("gas_2024_summer", "2024-07-01", 0.76),
        ("gas_2024_summer", "2024-08-01", 0.72),
        ("gas_2024_summer", "2024-09-01", 0.64),
        ("conflict_red_sea", "2024-01-01", 0.38),
        ("conflict_red_sea", "2024-01-15", 0.57),
        ("conflict_red_sea", "2024-02-01", 0.72),
        ("conflict_red_sea", "2024-02-15", 0.83),
        ("conflict_red_sea", "2024-03-01", 0.88),
        ("conflict_red_sea", "2024-03-20", 0.91),
        ("conflict_ceasefire", "2024-02-01", 0.46),
        ("conflict_ceasefire", "2024-03-01", 0.39),
        ("conflict_ceasefire", "2024-04-01", 0.34),
        ("conflict_ceasefire", "2024-05-01", 0.28),
        ("conflict_ceasefire", "2024-05-25", 0.19),
        ("election_senate", "2024-07-01", 0.44),
        ("election_senate", "2024-08-01", 0.47),
        ("election_senate", "2024-09-01", 0.53),
        ("election_senate", "2024-10-01", 0.59),
        ("election_senate", "2024-10-25", 0.64),
        ("election_senate", "2024-11-05", 0.68),
        ("election_turnout", "2024-07-01", 0.61),
        ("election_turnout", "2024-08-01", 0.58),
        ("election_turnout", "2024-09-01", 0.49),
        ("election_turnout", "2024-10-01", 0.43),
        ("election_turnout", "2024-11-05", 0.35),
    ],
    columns=["market_id", "date", "probability"],
)


GROUND_TRUTH = pd.DataFrame(
    [
        ("gas_2024_spike", "2024-04-01", 3.52, "gas_price"),
        ("gas_2024_spike", "2024-05-01", 3.59, "gas_price"),
        ("gas_2024_spike", "2024-06-01", 3.48, "gas_price"),
        ("gas_2024_spike", "2024-07-01", 3.44, "gas_price"),
        ("gas_2024_spike", "2024-08-01", 3.38, "gas_price"),
        ("gas_2024_spike", "2024-09-01", 3.31, "gas_price"),
        ("gas_2024_summer", "2024-04-01", 3.44, "gas_price"),
        ("gas_2024_summer", "2024-05-01", 3.57, "gas_price"),
        ("gas_2024_summer", "2024-06-01", 3.64, "gas_price"),
        ("gas_2024_summer", "2024-07-01", 3.69, "gas_price"),
        ("gas_2024_summer", "2024-08-01", 3.61, "gas_price"),
        ("gas_2024_summer", "2024-09-01", 3.52, "gas_price"),
        ("conflict_red_sea", "2024-01-12", 1.0, "event: Shipping advisories expanded"),
        ("conflict_red_sea", "2024-02-03", 1.0, "event: Rerouting costs rose"),
        ("conflict_red_sea", "2024-03-18", 1.0, "event: Disruptions still active"),
        ("conflict_ceasefire", "2024-02-20", 1.0, "event: Talks opened"),
        ("conflict_ceasefire", "2024-04-12", 1.0, "event: Negotiations stalled"),
        ("conflict_ceasefire", "2024-05-28", 1.0, "event: No durable deal"),
        ("election_senate", "2024-07-01", 47.0, "polling"),
        ("election_senate", "2024-08-01", 48.5, "polling"),
        ("election_senate", "2024-09-01", 50.2, "polling"),
        ("election_senate", "2024-10-01", 51.0, "polling"),
        ("election_senate", "2024-11-01", 51.7, "polling"),
        ("election_turnout", "2024-07-01", 55.0, "polling"),
        ("election_turnout", "2024-08-01", 54.4, "polling"),
        ("election_turnout", "2024-09-01", 53.1, "polling"),
        ("election_turnout", "2024-10-01", 52.7, "polling"),
        ("election_turnout", "2024-11-01", 51.9, "polling"),
    ],
    columns=["market_id", "date", "value", "series"],
)


def load_markets(topic: str | None = None) -> pd.DataFrame:
    markets = MARKETS.copy()
    if topic is not None:
        markets = markets[markets["topic"] == topic]
    return markets.reset_index(drop=True)


def load_probabilities(market_id: str) -> pd.DataFrame:
    return _load_market_series(PROBABILITIES, market_id)


def load_ground_truth(market_id: str) -> pd.DataFrame:
    return _load_market_series(GROUND_TRUTH, market_id)


def _load_market_series(source: pd.DataFrame, market_id: str) -> pd.DataFrame:
    data = source[source["market_id"] == market_id].copy()
    data["date"] = pd.to_datetime(data["date"])
    return data.reset_index(drop=True)

# Prediction Markets vs Reality

An interactive analytics app that evaluates how well prediction markets forecast real-world outcomes across economics, geopolitics, and elections.

## Overview

Prediction markets like Polymarket provide real-time probabilities for future events.  
This project investigates a key question:

> Are these probabilities actually meaningful forecasts?

The app compares market predictions against real-world outcomes to evaluate:
- Accuracy
- Calibration (probability vs reality)
- Timing (prediction vs reaction)

---

## Features

### Cross-Domain Analysis
- Gas Prices (economic indicators)
- Foreign Conflict (geopolitical events)
- Elections / Politics (polling vs outcomes)

### Market Evaluation
- Probability over time
- Real-world outcome overlays
- Resolution tracking

### Metrics
- Brier Score (forecast accuracy)
- Calibration insights
- Time-to-confidence (when market "decided")
- Volatility of predictions

---

## Example Questions

- Do prediction markets anticipate gas price spikes?
- Do they move before or after major geopolitical events?
- Are they more reliable than polling in elections?

---

## Tech Stack

- Python
- Streamlit (web app)
- DuckDB (data storage)
- Pandas (data processing)

---

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
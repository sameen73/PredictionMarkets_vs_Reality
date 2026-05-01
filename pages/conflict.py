import plotly.graph_objects as go
import streamlit as st

from utils.data_loader import load_ground_truth, load_markets, load_probabilities
from utils.metrics import brier_score, probability_volatility, time_to_threshold


TOPIC = "conflict"


def select_market():
    markets = load_markets(TOPIC)
    selected_label = st.selectbox("Select a market", markets["label"])
    return markets[markets["label"] == selected_label].iloc[0]


def render_summary(market, probabilities) -> None:
    outcome = int(market["outcome"])
    threshold_date = time_to_threshold(probabilities)

    st.subheader("Summary")
    st.write(f"**Question:** {market['question']}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Final probability", f"{probabilities['probability'].iloc[-1]:.0%}")
    col2.metric("Outcome", "Yes" if outcome else "No")
    col3.metric("Brier score", f"{brier_score(probabilities['probability'], outcome):.3f}")

    detail1, detail2 = st.columns(2)
    detail1.metric("Time to 70%", format_threshold_date(threshold_date))
    detail2.metric("Volatility", f"{probability_volatility(probabilities['probability']):.3f}")


def format_threshold_date(threshold_date) -> str:
    if threshold_date is None:
        return "Not reached"
    return threshold_date.strftime("%b %d, %Y")


def build_chart(probabilities, events) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=probabilities["date"],
            y=probabilities["probability"],
            mode="lines+markers",
            name="Market probability",
        )
    )
    for _, event in events.iterrows():
        fig.add_trace(
            go.Scatter(
                x=[event["date"], event["date"]],
                y=[0, 1],
                mode="lines",
                line=dict(color="#dc2626", dash="dot"),
                name=event["series"].replace("event: ", ""),
                hovertemplate="%{fullData.name}<extra></extra>",
                showlegend=True,
            )
        )
    fig.update_layout(
        xaxis_title="Time",
        yaxis=dict(title="Probability", range=[0, 1], tickformat=".0%"),
        hovermode="x unified",
        margin=dict(l=8, r=8, t=24, b=8),
    )
    return fig


def main() -> None:
    st.set_page_config(page_title="Foreign Conflict", page_icon=":warning:", layout="wide")
    st.title("Foreign Conflict")

    market = select_market()
    probabilities = load_probabilities(market["market_id"])
    events = load_ground_truth(market["market_id"])

    render_summary(market, probabilities)
    st.plotly_chart(build_chart(probabilities, events), width="stretch")


main()

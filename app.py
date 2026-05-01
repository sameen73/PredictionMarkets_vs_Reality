import streamlit as st


def main() -> None:
    st.set_page_config(
        page_title="Prediction Markets vs Reality",
        page_icon=":bar_chart:",
        layout="wide",
    )

    st.title("Prediction Markets vs Reality")
    st.write(
        "This MVP compares prediction market probabilities against real-world outcomes "
        "across gas prices, foreign conflict, and elections/politics."
    )

    st.subheader("Navigation")
    st.write("Use the sidebar to open one of the topic pages:")
    st.markdown(
        """
        - **Gas Prices**: compare market probabilities with a mock fuel-price series.
        - **Foreign Conflict**: compare probability movement with mock event markers.
        - **Elections / Politics**: compare market probabilities with mock polling data.
        """
    )

    st.info("All data in this scaffold is mock data for local MVP development.")


main()

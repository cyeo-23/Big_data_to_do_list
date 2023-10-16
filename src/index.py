"""
This module provides the main functionality for the Streamlit application.
"""

import streamlit as st
from utils.st_utils import footer


def main():
    """Display the main Streamlit application page."""

    st.set_page_config(layout="wide", page_title="You do", page_icon="📜")

    # Styling for the page
    st.markdown(
        """<style>.font {
            font-size:35px;
            font-family: 'Cooper Black';
            color: white;
            }
        </style>""", unsafe_allow_html=True
    )

    st.markdown('<p class="font">Accueil</p>', unsafe_allow_html=True)

    st.sidebar.success("Select an option above.")

    kpi2, kpi4 = st.columns(2)

    # Styles for metrics
    metric_style = """<style>
        align-items: center;
        display: flex;
        flex-direction: column;
        </style>"""

    kpi4.markdown(metric_style, unsafe_allow_html=True)
    kpi2.markdown(metric_style, unsafe_allow_html=True)

    kpi4.metric(label="Metric 2", value=5)
    kpi2.metric(label="Metric 1", value=456)

    footer()


if __name__ == "__main__":
    main()

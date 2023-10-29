"""Module to display the tasks page in the Streamlit application."""
import streamlit as st
from utils.st_utils import footer, nav_page


def display_page():
    """Display the Streamlit page for tasks."""
    st.set_page_config(layout="wide", page_title="You do", page_icon="📜")

    st.markdown(
        """<style>.font {
        font-size:35px ; font-family: 'Cooper Black'; color: white;}
        </style>""",
        unsafe_allow_html=True
    )
    st.markdown('<p class="font">Tasks</p>', unsafe_allow_html=True)
    st.write(f"Connecté avec l'ID: {st.session_state.user.id}")

    footer()


if __name__ == "__main__":
    if 'user' not in st.session_state:
        nav_page("")
    else:
        display_page()

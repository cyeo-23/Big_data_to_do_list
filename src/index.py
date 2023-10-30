"""This module provides the main functionality."""
import streamlit as st
from utils.st_utils import footer, nav_page
from utils.logger import Logger
from services.user_services import UserServices

log = Logger(__name__)


# Page de connexion
def login_page(service: UserServices):
    """Display the login page."""
    st.title("Page de Connexion")
    pseudo = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        user = service.connect_user(pseudo=pseudo, password=password)
        if user:
            st.session_state['user'] = user
            nav_page("tasks")
        else:
            st.error("Identifiants incorrects")


def main():
    """Display the main Streamlit application page."""
    st.set_page_config(page_title="Connexion page", page_icon="👥")

    # Styling for the page
    st.markdown(
        """<style>.font {
            font-size:35px;
            font-family: 'Cooper Black';
            color: white;
            }
        </style>""", unsafe_allow_html=True
    )

    st.sidebar.success("Select an option above.")
    service = UserServices()

    if 'user' not in st.session_state:
        login_page(service)
    else:
        nav_page("tasks")

    footer()


if __name__ == "__main__":
    main()

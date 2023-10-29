"""This module provides the main functionality."""
import argon2
import streamlit as st
from utils.st_utils import footer, nav_page
from utils.logger import Logger
from services.user_services import UserServices
from models.user import User

log = Logger(__name__)
password_hasher = argon2.PasswordHasher()


def update_user_page(user: User):
    """Updade User page."""
    service = UserServices()
    st.title("Modifier mon compte")
    old_password = st.text_input("Ancien mot de Passe", type="password")
    new_password = st.text_input("Nouveau mot de Passe", type="password")
    firstname = st.text_input("Prenom(s)", user.firstname)
    lastname = st.text_input("Nom(s)", user.lastname)
    if st.button("Mettre à jour"):
        try:
            if password_hasher.verify(user.password, old_password):
                user.firstname = firstname
                user.lastname = lastname
                user.password = new_password
                try:
                    service.update_user(user)
                    nav_page("update_user")
                except Exception as e:
                    log.log_error(f"Une erreur inattendue s'est produite: {e}")
                else:
                    st.success("Modification effectuée avec succès")
            else:
                st.error("L'ancien password est différent de celui saisi")
        except Exception as e:
            st.error("L'ancien password est différent de celui saisi")
            log.log_error(f"Une erreur inattendue s'est produite: {e}")


def main():
    """Display the main Streamlit application page."""
    st.set_page_config(page_title="User profile", page_icon="👥")

    # Styling for the page
    st.markdown(
        """<style>.font {
            font-size:35px;
            font-family: 'Cooper Black';
            color: white;
            }
        </style>""", unsafe_allow_html=True
    )

    if 'user' not in st.session_state:
        nav_page("")
    else:
        update_user_page(st.session_state.user)

    footer()


if __name__ == "__main__":
    main()

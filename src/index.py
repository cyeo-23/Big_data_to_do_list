"""This module provides the main functionality."""
import streamlit as st
from utils.st_utils import footer
from utils.logger import Logger
from services.user_services import UserServices 
from models.user import User 

log = Logger(__name__)

# Page de connexion

def login_page(service: UserServices):
    st.title("Page de Connexion")
    pseudo = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        user = service.connect_user(pseudo=pseudo, password=password)
        print(f"User: {user}")
        if user:
            st.success(f"Connecté en tant que {user.pseudo} (ID: {user.id})")
            st.session_state['user_id'] = user.id  # Stocker l'ID de l'utilisateur en session
        else:
            st.error("Identifiants incorrects")
            
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
    service = UserServices()

    if 'user_id' not in st.session_state:
        login_page(service)
    else:
        st.title("Page d'accueil")
        st.write(f"Connecté en tant qu'utilisateur avec l'ID: {st.session_state.user_id}")

    footer()


if __name__ == "__main__":
    main()

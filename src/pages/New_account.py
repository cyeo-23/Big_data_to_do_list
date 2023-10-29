"""This module provides the main functionality."""
import streamlit as st
from utils.st_utils import footer
from utils.logger import Logger
from services.user_services import UserServices 
from models.user import User 

log = Logger(__name__)

def create_account_page(service: UserServices):
    st.title("Créer un Compte")
    pseudo = st.text_input("Nom d'Utilisateur")
    password = st.text_input("Mot de Passe", type="password")
    firstname = st.text_input("Prenom(s)")
    lastname = st.text_input("Nom(s)")
    if st.button("Creer"):
        new_user = User(firstname=firstname, lastname=lastname, password=password, pseudo=pseudo)
        try :
            user = service.add_user(new_user)
            print(user)
        except Exception as e :
            log.log_error(f"Une erreur inattendue s'est produite: {e}")
        else :
            st.success("Compte créé avec succès. Vous pouvez maintenant vous connecter.")
   
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
    try :
        service = UserServices()
    except Exception as e :
        print(e)

    if 'user_id' not in st.session_state:
        create_account_page(service)
    else:
        st.title("Page d'accueil")
        st.write(f"Connecté en tant qu'utilisateur avec l'ID: {st.session_state.user_id}")

    footer()


if __name__ == "__main__":
    main()

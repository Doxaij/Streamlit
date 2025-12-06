# Module streamlit
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# bibliotheques
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import time

# Importation du module
import yaml
from yaml.loader import SafeLoader


# Titre principal de l'application (affiché en haut de la page)
st.title("Bienvenue")

# Elements textuels d'information pour la connexion
st.markdown("Veuillez saisir votre identifiant et mot de passe pour accéder au contenu", width='stretch')
st.text("Username: utilisateur\nPassword: 0000")

# d'abord charger cela 
with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# pour que les variables config fonctionne et se réfère au fichier credentials
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

authenticator.login()
auth_status = st.session_state.get("authentication_status")

# === PORTAIL D'AUTHENTIFICATION ===

if st.session_state["authentication_status"]:
    authenticator.logout("Déconnexion", "sidebar")
    st.write(f"Bienvenue {st.session_state['name']}")
elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")
else:
    st.warning("Veuillez entrer un nom d'utilisateur et un mot de passe")


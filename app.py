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

# d'abrod charger cela 
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
    authenticator.logout()
    st.write(f"Bienvenue {st.session_state['name']}")
elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")
else:
    st.warning("Veuillez entrer un nom d'utilisateur et un mot de passe")


# === À PARTIR D'ICI : CONTENU RÉSERVÉ AUX UTILISATEURS CONNECTÉS ===
st.write("Hello World")

# Titre principal de l'application (affiché en haut de la page)
st.title("The title of my page")

# Titre de section important (taille 1)
st.header("An Important Header")

# Sous-titre (taille 2), utile pour organiser le contenu par sous-sections
st.subheader("A Secondary Header")

# Affiche une ligne de texte simple (sans mise en forme particulière)
st.text("My classic text")

# Affiche du texte avec mise en forme Markdown
st.markdown(''':rainbow: :rainbow[My markdown]''')  # Ici, un effet arc-en-ciel est appliqué

# Affiche un dataframe (st.write accepte plusieurs arguments et plusieurs types de données)
st.write(
    pd.DataFrame({
            "Cards": ['Name 1', 'Name 2', 'Name 3', 'Name 4'],
            "Quantity": [0, 1, 0, 3]}
    )
)
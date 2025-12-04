# j'importe les bibliothèques
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import time
# Importation du module
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate





# Création du menu qui va afficher les choix qui se trouvent dans la variable options
selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")
# ... et ainsi de suite pour les autres pages


# Création de 3 colonnes 
col1, col2, col3 = st.columns(3)


# Contenu de la première colonne : 
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")


# Contenu de la deuxième colonne :
with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")


# Contenu de la troisième colonne : 
with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")

 # Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
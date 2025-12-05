import streamlit as st
import pandas as pd

# --- AUTHENTIFICATION OBLIGATOIRE POUR AFFICHER ---
auth_status = st.session_state.get("authentication_status")
if not auth_status:
    st.warning("Accès réservé. Merci de vous connecter sur la page 'app'.")
    st.stop()

df = pd.read_csv(r"C:\Users\33631\Downloads\Formation\Streamlit\Partie_1\streamlit\data\taxis.csv")
pb_liste = list(df['pickup_borough'].dropna().unique())

st.title("Bienvenue sur le site web de Margie")
choix = st.selectbox("Indiquez votre arrondissement de récupération",
             pb_liste) 

if choix == pb_liste[0]:
    st.write(f'Tu as choisis: {pb_liste[0]}')
    st.image("https://www.nyc.fr/wp-content/uploads/2015/08/nyc-scaled.jpg")
if choix == pb_liste[1]:
    st.write(f'Tu as choisis: {pb_liste[1]}')
    st.image("https://media.cnewyork.net/resize/uploads/2023/04/long-island-city.jpg?format=auto")
if choix == pb_liste[2]:
    st.write(f'Tu as choisis: {pb_liste[2]}')
    st.image("https://bonjournewyork.fr/wp-content/uploads/2023/11/quartiers-de-nyc.jpg")
if choix == pb_liste[3]:
    st.write(f'Tu as choisis: {pb_liste[3]}')
    st.image("https://www.partir-a-new-york.com/wp-content/uploads/2022/05/brooklyn-heights.jpg")

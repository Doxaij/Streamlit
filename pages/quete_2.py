# j'importe les bibliothèques
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

# --- AUTHENTIFICATION OBLIGATOIRE POUR AFFICHER ---
auth_status = st.session_state.get("authentication_status")
if not auth_status:
    st.warning("Accès réservé. Merci de vous connecter sur la page 'app'.")
    st.stop()


# Je fais un peu de fioriture, texte, présentation
st.title("Bienvenue sur le site web de Margie")

st.subheader("Manipulation de données et création de graphiques")

# charger le dataset
geyser  = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/geyser.csv")
vols = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

df_vols = pd.DataFrame(vols)
df_iris = pd.DataFrame(iris)
liste = st.selectbox("Quel sujet veux tu étudier?",
             ['vols','iris', 'geyser'])


if liste == 'vols':
    df = df_vols
    st.dataframe(df)
    colonne_x = st.selectbox("Choisissez les données à placer sur l'axe X:",
             df.columns.drop('month'))

    colonne_y = st.selectbox("Choisissez les données à placer sur l'axe Y:",
             df.columns.drop('month'))
    st.image("https://www.guidesulysse.com/images/destinations/iStock-610775136.jpg")

if liste == 'iris':
    df = df_iris
    st.dataframe(df)
    colonne_x = st.selectbox("Choisissez les données à placer sur l'axe X:",
             df.columns.drop('species'))

    colonne_y = st.selectbox("Choisissez les données à placer sur l'axe Y:",
             df.columns.drop('species'))
    st.image("https://cdn.jacques-briant.fr/4455/iris-de-hollande.jpg", width='stretch')    

if liste == 'geyser':
    df= geyser
    st.dataframe(df)
    colonne_x = st.selectbox("Choisissez les données à placer sur l'axe X:",
             df.columns.drop('kind'))

    colonne_y = st.selectbox("Choisissez les données à placer sur l'axe Y:",
             df.columns.drop('kind'))
    # une image vaut mille mots
    st.image("https://www.voyage-islande.com/upload/auto/islande/830x830/geysir-islande_6704f4d0849cc5.27464929.webp")
    # un peu d'audio pour une immersion sympa
    st.write("Les glouglous bizarre d'un geyser")
    st.audio("https://sounds-mp3.com/mp3/0000646.mp3")


graphique = st.selectbox("Quel graphique veux-tu utiliser",
             ['Graphique en barre','Nuage de points','Graphique linéaire'])

#mise en forme des tritres et sous titres
if graphique == 'Nuage de points':
    st.header('Graphique Nuage de points', divider="green")
    if liste == 'geyser':
        st.subheader("Interdépendance entre éruption et attente :hourglass:")
    # des petits émojis par ce que c'est rigolo
    st.scatter_chart(data=df, 
                    x=colonne_x,
                    y=colonne_y 
                    )

if graphique == 'Graphique en barre':                    
    st.header('Graphique en barres', divider="red")
    if liste == 'geyser':
        st.subheader("Les temps d’attente les plus fréquents\nÀ quel point doit-on attendre avant qu’un geyser explose ? :sweat_drops:")
    st.bar_chart(data=df, 
                    x=colonne_x, 
                    y=colonne_y 
                    )

if graphique == "Graphique linéaire":
    st.header('Graphique linéaire', divider="yellow")
    if liste == 'geyser':
        st.subheader("Relation entre la durée d’éruption et le temps d’attente\nOù comment la durée d’un geyser influence-t-elle l’attente avant le suivant ? :ocean:")
    st.line_chart(data=df, 
                    x=colonne_x, 
                    y=colonne_y
                   )

# je stock la variation "on" du bouton dans une variablr
on = st.toggle("Afficher la matrice de corrélation", value=True) #Ici, il est activé par défaut (value=True).
st.write('___', )

#condition: si on alors j'affiche la matrice
if on:
    correlation = df.corr(numeric_only=True)
    st.subheader('Matrice de Corrélation', divider="blue")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(
        correlation,
        ax=ax,
        annot=True,       # affiche les valeurs dans les cases
        cmap="coolwarm",  # palette de couleurs 
        center=0
    )
    st.pyplot(fig)

# Et un petit GIF parce que c'est mimi =)
    if liste == 'vols':
        st.image("https://www.linternaute.com/_montage/week-end/buzz/wanderlust/10.gif", width='stretch')
    if liste == 'iris':
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnByNXpubms4Ym5mMmRobDU4cGhzOGZvMmhiOXEzam5kOWV2bTBkOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eoAuF3XZe84riCbE5O/giphy.gif",width='stretch')
    if liste == 'geyser':
        st.image("https://i.pinimg.com/originals/03/57/f4/0357f40e3ca8684a9ddb853498b1a7a8.gif", width="stretch" )

if st.sidebar.button("Déconnexion"):
    st.session_state.clear()
    st.rerun()    
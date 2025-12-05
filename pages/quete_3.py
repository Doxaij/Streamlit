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

# --- AUTHENTIFICATION OBLIGATOIRE POUR AFFICHER ---
auth_status = st.session_state.get("authentication_status")
if not auth_status:
    st.warning("Accès réservé. Merci de vous connecter sur la page 'app'.")
    st.stop()





# Création du menu qui va afficher les choix qui se trouvent dans la variable options
with st.sidebar:
    selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Wiki des chats", "Galerie", "Wiki du chat moderne"]
        )

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.title("🐾 Bienvenue sur CatHub")
    st.subheader("Le portail qui explore toutes les facettes du mot « chat »")

    st.markdown(
        """
        Cette application te propose un parcours simple et ludique autour de trois univers :

        - **Wiki du Chat** : une page dédiée au chat domestique à son histoire à son comportement et à ses particularités  
        - **Galerie de Chats** : un espace visuel pour admirer une sélection d’images félines  
        - **Wiki du Chat Moderne (ChatGPT)** : une exploration du “chat” au sens numérique avec une présentation accessible de ChatGPT et de l’IA conversationnelle  
        

        Utilise le menu à gauche pour naviguer entre les différentes sections.  
        Bonne visite parmi les chats d’hier d’aujourd’hui et du numérique 🐱✨
        """
    )



elif selection == "Wiki des chats":
    st.header("Wiki Félins domestiques")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Felis silvestris catus")
        st.text("Le chat domestique (Felis catus ou Felis silvestris catus) est la forme domestique du chat sauvage Felis silvestris, une espèce de mammifères carnivores, de la famille des Félidés.\nSelon les résultats de travaux menés en 2006 et 2007[1], le chat domestique est une sous-espèce du chat sauvage issue d'ancêtres appartenant à la sous-espèce du chat sauvage d'Afrique (Felis silvestris lybica). Les premières domestications ont probablement lieu il y a 8 000 à 10 000 ans au Néolithique dans le Croissant fertile, époque correspondant au début de la culture de céréales et à l'engrangement de réserves susceptibles d'être attaquées par des rongeurs, le chat devenant alors pour l'Homme un auxiliaire utile se prêtant à la domestication.") 
        st.text("Le chat domestique est l'un des principaux animaux de compagnie et compte aujourd'hui une cinquantaine de races différentes reconnues par les instances de certification. Dans de très nombreux pays, le chat entre dans le cadre de la législation sur les carnivores domestiques à l'instar du chien et du furet. Essentiellement territorial, le chat est un prédateur de petites proies comme les rongeurs ou les oiseaux. Les chats ont diverses vocalisations dont les ronronnements, les miaulements, les feulements ou les grognements, bien qu'ils communiquent principalement par des positions faciales et corporelles et des phéromones.")
        st.text("Tout d'abord vénéré par les Égyptiens, il est diabolisé en Europe au Moyen Âge et ne retrouve ses lettres de noblesse qu'au XVIIIe siècle. En Asie, le chat reste synonyme de chance, de richesse ou de longévité. Ce félin laisse son empreinte dans la culture populaire et artistique, tant au travers d'expressions populaires que de représentations diverses au sein de la littérature, de la peinture ou encore de la musique. À partir de la fin du XXe siècle, les dommages qu'il occasionne à la biodiversité sont mieux compris, et il fait partie des cent espèces envahissantes parmi les plus nuisibles du monde.")    
        link = "https://fr.wikipedia.org/wiki/Chat"
        st.markdown(f"Source des informations {link}")
    with col2:
        st.image("https://i.pinimg.com/736x/aa/f1/0b/aaf10bb1f68836b07d534f06455c01e7.jpg")



elif selection == "Galerie":
    st.header("Bienvenue sur la galerie des félins")
# ... et ainsi de suite pour les autres pages
    # Création de 3 colonnes 
    col1, col2, col3 = st.columns(3)

    # Contenu de la première colonne : 
    with col1:
        st.header("Chat Abyssin")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDFR4ZcYvvJyRZROCSRdJOi3bFZXPwvR-fjQ&s")


    # Contenu de la deuxième colonne :
    with col2:
        st.header("Chat Siamois")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Siamese_cat_Vaillante.JPG/330px-Siamese_cat_Vaillante.JPG")


    # Contenu de la troisième colonne : 
    with col3:
        st.header("Chat Bengale")
        st.image("https://www.zooplus.fr/magazine/wp-content/uploads/2018/02/schnee-bengal-katze.webp")

elif selection == "Wiki du chat moderne":
    st.header("Wiki du Chat GPT")
    st.text("ChatGPT est un agent conversationnel (chatbot) développé par OpenAI. Depuis août 2025, ChatGPT se base sur GPT-5, un transformeur génératif préentraîné, pour générer du texte.")
    st.text("ChatGPT est capable de répondre à des questions, de tenir des conversations, de générer du code informatique, de faire des recherches sur Internet, d'écrire, de traduire ou encore de synthétiser des textes. Il peut le faire en tenant compte du contexte et de contraintes telles que le style d'écriture. Il peut aussi servir d'assistant vocal ou générer des images. Les abonnements payants (ChatGPT « Plus », « Team » et « Enterprise ») offrent un seuil d'utilisation plus élevé, ainsi que des fonctionnalités supplémentaires.")
    st.text("En raison de ses multiples capacités, ChatGPT suscite des inquiétudes quant aux risques de détournement à des fins malveillantes, de plagiat dans le monde universitaire et de suppressions d'emplois dans certains secteurs, en plus de soulever des préoccupations en matière de sécurité et de désinformation, car le modèle peut être utilisé pour créer des textes faux et des informations trompeuses.")
    st.text("ChatGPT est lancé en novembre 2022 dans une version gratuite où il n'a pas accès à Internet comme source d'informations. Il bénéficie aussitôt d’une large exposition médiatique et reçoit un accueil globalement positif, bien que son exactitude factuelle soit critiquée. En janvier 2023, ChatGPT compte plus de 100 millions de comptes enregistrés, et la société OpenAI est alors valorisée à 29 milliards de dollars américains. ")
    link = "https://fr.wikipedia.org/wiki/ChatGPT"
    st.markdown(f"Source des informations {link}")



if st.sidebar.button("Déconnexion"):
    st.session_state.clear()
    st.rerun()    
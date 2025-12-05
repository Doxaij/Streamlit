import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# j'importe les bibliothèques
import streamlit as st
# Titre de la page
st.title("Manipulation de données et création de graphiques")

# Création des datasets et graphiques disponibles
liste = ['','flights','planets','diamonds']
liste_graph = ['','scatter_chart','line_chart','bar_chart']


# Selection & affichage du dataset
selection = st.selectbox("Quel dataset veux-tu utiliser ?", liste)

if selection !="":
    df = sns.load_dataset(selection)
    st.dataframe(df.head(10))

# Choix des x & y
if selection !="":
    columns = list(df.columns) # list -> garanti que la valeur reste vide par défaut, évite que ce soit la 1 col du dataset qui s'affiche
else:
    columns = ['']
col_x = st.selectbox("Choississez la colonne X",['']+columns) # [''] -> option vide au début
col_y = st.selectbox("Choississez la colonne Y",['']+columns)

# Affichage des graphiques
graph = st.selectbox("Quel graphique veux-tu visualiser ?", liste_graph)
if selection !="" and graph !="":
    if graph == 'scatter_chart':
        sns.scatterplot(x=col_x, y=col_y, data=df)
    elif graph == 'line_chart':
        sns.lineplot(x=col_x, y=col_y, data=df)
    elif graph == 'bar_chart':
        sns.barplot(x=col_x, y=col_y, data=df)
    else:
        liste_graph == ""

    plt.xticks(rotation=45, ha='right')
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    st.pyplot(plt.gcf())

# Affichage matrice de correlation
matrice = st.checkbox("Afficher la matrice de corrélation")

if matrice:
    if pd.api.types.is_numeric_dtype(df[col_x]) and pd.api.types.is_numeric_dtype(df[col_y]):
    # pd.api.types.is_numeric_dtype -> vérifie si le type de données fournies est numérique
        df_corr = df[[col_x,col_y]].corr()
        sns.heatmap(df_corr, cmap='cividis')
        st.pyplot(plt.gcf())
    else:
        st.write("La matrice de corrélation ne fonctionne que sur des colonnes numériques")
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Titre principal de l'application (affiché en haut de la page)
st.title("Manipulation de données et création de graphiques")

st.write("\n\n")

flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

df_flights = pd.DataFrame(flights)
df_iris = pd.DataFrame(iris)

liste = st.selectbox("Quel dataset veux-tu utiliser",
             ['flights','iris'])

if liste == 'flights':
    df = df_flights
elif liste == 'iris':
    df = df_iris

st.dataframe(df)

colonne_x = st.selectbox("Choisissez la colonne X",
             ['year','month','passengers'])

colonne_y = st.selectbox("Choisissez la colonne Y",
             ['year','month','passengers'])

graphique = st.selectbox("Quel graphique veux-tu utiliser",
             ['bar_chart','scatter_chart','line_chart'])



fig, ax = plt.subplots()

if graphique == "bar_chart":
    sns.barplot(x=colonne_x, y=colonne_y, data=df, ax=ax)
elif graphique == "scatter_chart":
   fig, ax = plt.subplots()
   sns.scatterplot(x=colonne_x, y=colonne_y, data=df, ax=ax)
#streamlit run Antho_quêtes2_streamlit.pyelif graphique == "line_chart":
   sns.lineplot(x=colonne_x, y=colonne_y, data=df, ax=ax)

st.pyplot(fig)


case = st.checkbox("Afficher la matrice de corrélation")
numeric_df = df_flights.select_dtypes(include='number')
correlation = numeric_df.corr()


if case == True :
    fig2, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig2)
else:
    ""
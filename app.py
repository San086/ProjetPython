import streamlit as st
import pandas as pd
import numpy as np
import math


st.title('Projet oiseaux :bird: de :blue[Marseille] :sunglasses:')
st.text("Lea COQUEREAU\nGuillaume VALENTIN\nAndreas JULIEN-CARAGUEL")
st.header("Problématique", divider="gray")
st.text("Comment sont différentes espèces d'oiseaux de Marseille sont-elle réparti dans la ville ?")

fichier = "marseille_biodiversite_oiseaux_parcs.csv"
data = pd.read_csv(fichier)

st.header("Tableau de données", divider=True)
data.insert(0, 'ID', range(1, 1 + len(data)))
df = pd.DataFrame(data)
df


st.header("Distribution des noms des sites", divider=True)
bar = df["Nom du site"].str.split(" ;").str[0]
st.scatter_chart(bar)

st.header("Distribution des types", divider=True)
ty = df["Type"]
st.scatter_chart(ty)

st.header("Nombre d'espèces observer par parc", divider=True)
df_grouped = df.groupby("Période d'observation")["Nom du site"].first().reset_index()
st.scatter_chart(df_grouped)

st.header("Nombre d'observation par espèce à Marseille", divider=True)
ver = df["Nom vernaculaire"]
st.scatter_chart(ver)


st.header("Tableau du nombre d'espèce", divider=True)
tab1 = data["Nom vernaculaire"].value_counts()
tab1

st.header("Tableau de répartition des espèces dans les parcs", divider=True)
parcs_vernaculaires = data.groupby("Nom du site")["Nom vernaculaire"].apply(list).reset_index()
parcs_vernaculaires

st.header("Tableau récapitulatif avec d'autres trucs", divider=True)
arcs = pd.DataFrame({
    "Nom du site": data["Nom du site"].unique(),
    "Nombre d'espèces observées": data.groupby("Nom du site")["Nom vernaculaire"].nunique().values,
    "Type": data.groupby("Nom du site")["Type"].first().values,  # Supposons que chaque parc ait un seul type
    "Espèces observées": data.groupby("Nom du site")["Nom vernaculaire"].apply(list).values,
    "Adresse": data.groupby("Nom du site")["Adresse"].first().values,  # Supposons que chaque parc ait une adresse unique
    "Latitude": data.groupby("Nom du site")["Latitude"].first().values,
    "Longitude": data.groupby("Nom du site")["Longitude"].first().values
})

arcs



st.header("Répartition des oiseaux dans Marseille (sans fond de carte)", divider=True)

# Création d'une carte avec les points des coordonnées
st.header("Carte des observations des oiseaux")
try:
    mappy = data[['Latitude', 'Longitude']].dropna()  # Retirer les lignes avec des valeurs manquantes
    st.map(mappy)
except Exception as e:
    st.error(f"Une erreur est survenue lors de la création de la carte : {e}")


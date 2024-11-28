import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt


st.title('Projet oiseaux :bird: de :blue[Marseille] :sunglasses:')
st.text("Lea COQUEREAU\nGuillaume VALENTIN\nAndreas JULIEN-CARAGUEL\n")
st.header("Problématique", divider="gray")
st.link_button("Source de la donnée", "https://www.data.gouv.fr/fr/datasets/marseille-biodiversite-oiseaux/")
st.text("Comment les différentes espèces d'oiseaux de Marseille sont-elle réparti dans la ville ?")


fichier = "marseille_biodiversite_oiseaux_parcs.csv"
data = pd.read_csv(fichier)

st.header("Tableau de données (brute)", divider=True)
data.insert(0, 'ID', range(1, 1 + len(data)))
df = pd.DataFrame(data)
df


#st.header("Distribution des noms des sites", divider=True)
#bar = df["Nom du site"].str.split(" ;").str[0]
#st.scatter_chart(bar)

#st.header("Distribution des types", divider=True)
#ty = df["Type"]
#st.scatter_chart(ty)

#st.header("Nombre d'espèces observer par parc", divider=True)
#df_grouped = df.groupby("Période d'observation")["Nom du site"].first().reset_index()
#st.scatter_chart(df_grouped)

#st.header("Nombre d'observation par espèce à Marseille", divider=True)
#ver = df["Nom vernaculaire"]
#st.scatter_chart(ver)


st.header("Tableau du nombre d'espèce", divider=True)
tab1 = data["Nom vernaculaire"].value_counts()
tab1

#st.header("Tableau de répartition des espèces dans les parcs", divider=True)
#parcs_vernaculaires = data.groupby("Nom du site")["Nom vernaculaire"].apply(list).reset_index()
#parcs_vernaculaires

st.header("Tableau récapitulatif de la répartition des espèces par parc", divider=True)
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


nom_vernaculaire_selection = st.selectbox(
    "Sélectionnez une espèce pour voir où elle a été observer :", 
    options=data["Nom vernaculaire"].unique(),
    index=None,
    placeholder="Selectionne une espèce d'oiseau...",
)

espece_info = data[data["Nom vernaculaire"] == nom_vernaculaire_selection]
sites_observes = espece_info["Nom du site"].unique()

st.write(f"**Sites où l'espèce '{nom_vernaculaire_selection}' a été observée :**")
st.dataframe(pd.DataFrame({"Nom du site": sites_observes}))

st.write(f"**Nombre total de sites où cette espèce a été observée :** {len(sites_observes)}")



st.header("Carte des observations des oiseaux", divider=True)

if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
    st.error("Le fichier doit contenir les colonnes 'Latitude' et 'Longitude'.")
    st.stop()

data = data.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

try:
    mappy = data[['latitude', 'longitude']].dropna() 
    st.map(mappy)
except Exception as e:
    st.error(f"Une erreur est survenue lors de la création de la carte : {e}")





st.link_button("Clique pour une surprise", "https://chat-jai-pete.fr/")










# Vérification de la colonne "Nom du site"
if "Nom du site" not in data.columns:
    st.error("La colonne 'Nom du site' est manquante dans les données.")
    st.stop()

# Comptage des occurrences par site
site_counts = data["Nom du site"].value_counts().reset_index()
site_counts.columns = ["Nom du site", "Fréquence"]

# Création du graphique avec Altair
chart = (
    alt.Chart(site_counts)
    .mark_bar(color="skyblue")
    .encode(
        x=alt.X("Nom du site", sort="-y", title="Nom du Site"),
        y=alt.Y("Nombre d'espèces observer", title="Nombre d'espèces observer"),
        tooltip=["Nom du site", "Nombre d'espèces observer"],
    )
    .properties(
        title="Distribution du nombre d'espèces observer dans chaque parcs",
        width=800,
        height=400,
    )
    .configure_axis(
        labelFontSize=12,
        titleFontSize=14,
    )
    .configure_title(fontSize=16)
)

# Affichage dans Streamlit
st.altair_chart(chart, use_container_width=True)

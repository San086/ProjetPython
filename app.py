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

st.header("Répartition des oiseaux dans Marseille (sans fond de carte)", divider=True)

st.header("Distribution des noms des sites", divider=True)
df["Simplified Nom du site"] = df["Nom du site"].str.split(" ;").str[0]
st.bar_chart(data, color="site", stack=False)


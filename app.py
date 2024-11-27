import streamlit as st
import pandas as pd
import numpy as np
import math

st.title('Projet oiseaux de Marseille !')
st.text("Lea COQUEREAU\nGuillaume VALENTIN\nAndreas JULIEN-CARAGUEL")


fichier = "marseille_biodiversite_oiseaux_parcs.csv"
data = pd.read_csv(fichier)

st.header("Tableau de données", divider=True)

df = pd.DataFrame(data)
df

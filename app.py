import streamlit as st
import pandas as pd
import numpy as np
import math

st.title('Projet oiseaux :bird: de :blue[Marseille] :sunglasses: !')
st.text("Lea COQUEREAU\nGuillaume VALENTIN\nAndreas JULIEN-CARAGUEL")


fichier = "marseille_biodiversite_oiseaux_parcs.csv"
data = pd.read_csv(fichier)

st.header("Tableau de données", divider=True)

df = pd.DataFrame(data)
df

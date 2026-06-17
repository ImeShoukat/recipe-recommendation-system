import pandas as pd
import streamlit as st
import recommendation_system_recepies as rec

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

st.title(
    "Food Recommendation System"
)

query = st.text_input(
    "Masukkan Nama Resep"
)

model = st.selectbox(
    "Pilih Model",
    ["Cosine", "KNN"]
)

if st.button("Cari"):

    if model == "Cosine":
        result = recommend_cosine(query)

    else:
        result = recommend_knn(query)

    st.dataframe(result)
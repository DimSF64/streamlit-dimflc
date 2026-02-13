import streamlit as st
import pandas as pd

st.set_page_config(page_title="DIMFLC App")

st.title("🚀 Application Streamlit DIMFLC")
st.write("Déployée avec YunoHost ✅")

name = st.text_input("Quel est ton nom ?")

if name:
    st.success(f"Bienvenue {name} 👋")

data = pd.DataFrame({
    "Année": [2023, 2024, 2025],
    "Utilisateurs": [120, 350, 890]
})

st.dataframe(data)

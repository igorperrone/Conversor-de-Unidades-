import streamlit as st

st.set_page_config(
    page_title="Conversor de Unidades",
    page_icon="🔄",
    layout="centered"
)

st.title("🔄 Conversor de Unidades")
st.write("Conversor desenvolvido em Python com Streamlit")

categoria = st.selectbox(
    "Categoria",
    ["Temperatura", "Distância", "Peso", "Volume"]
)

valor = st.number_input(
    "Digite o valor",
    value=0.0
)
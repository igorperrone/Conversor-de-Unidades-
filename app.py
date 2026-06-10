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

# TEMPERATURA
if categoria == "Temperatura":

    unidades = ["Celsius", "Fahrenheit", "Kelvin"]

    de = st.selectbox("De", unidades)
    para = st.selectbox("Para", unidades)

    if st.button("Converter"):

        resultado = valor

        if de == "Celsius" and para == "Fahrenheit":
            resultado = (valor * 9/5) + 32

        elif de == "Fahrenheit" and para == "Celsius":
            resultado = (valor - 32) * 5/9

        elif de == "Celsius" and para == "Kelvin":
            resultado = valor + 273.15

        elif de == "Kelvin" and para == "Celsius":
            resultado = valor - 273.15

        elif de == "Fahrenheit" and para == "Kelvin":
            resultado = (valor - 32) * 5/9 + 273.15

        elif de == "Kelvin" and para == "Fahrenheit":
            resultado = (valor - 273.15) * 9/5 + 32

        st.success(f"Resultado: {resultado:.4f} {para}")

# DISTÂNCIA
elif categoria == "Distância":

    unidades = {
        "Metros": 1,
        "Quilômetros": 1000,
        "Milhas": 1609.34
    }

    de = st.selectbox("De", list(unidades.keys()))
    para = st.selectbox("Para", list(unidades.keys()))

    if st.button("Converter"):

        resultado = valor * unidades[de] / unidades[para]

        st.success(f"Resultado: {resultado:.4f} {para}")

# PESO
elif categoria == "Peso":

    unidades = {
        "Quilos": 1,
        "Gramas": 0.001,
        "Libras": 0.453592
    }

    de = st.selectbox("De", list(unidades.keys()))
    para = st.selectbox("Para", list(unidades.keys()))

    if st.button("Converter"):

        resultado = valor * unidades[de] / unidades[para]

        st.success(f"Resultado: {resultado:.4f} {para}")

# VOLUME
elif categoria == "Volume":

    unidades = {
        "Litros": 1,
        "Mililitros": 0.001,
        "Galões": 3.78541
    }

    de = st.selectbox("De", list(unidades.keys()))
    para = st.selectbox("Para", list(unidades.keys()))

    if st.button("Converter"):

        resultado = valor * unidades[de] / unidades[para]

        st.success(f"Resultado: {resultado:.4f} {para}")
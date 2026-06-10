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

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

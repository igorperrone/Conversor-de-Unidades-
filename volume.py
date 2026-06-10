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
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

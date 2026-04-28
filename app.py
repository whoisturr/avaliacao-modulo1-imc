import streamlit as st

st.title("Calculadora IMC 📱")
st.subheader("Feito com Streamlit ❤️")

altura = st.number_input("digite a sua altura", min_value=0.0)
peso = st.number_input("digite o seu peso", min_value=0.0)

if st.button("Calcular"):
    imc = peso / altura ** 2
    st.info(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        st.error("Abaixo do peso.")
    elif imc < 24.9:
        st.success("Peso normal.")
    elif imc < 29.9:
        st.warning("Sobrepeso.")
    elif imc < 34.9:
        st.error("Obesidade Grau I")
    elif imc < 39.9:
        st.error("Obesidade Grau II")
    else:
        st.error("Obesidade Grau III")
    

import streamlit as st
import joblib
import pandas as pd

# Cargar modelo entrenado
model = joblib.load("model/best_model_rf.pkl")

st.title("Predicción de precios de casas en Ámsterdam🏡")

st.write("Introduce las características de la vivienda:")

# Inputs del usuario
area = st.number_input("Área (m²)", min_value=10, max_value=1000, value=90, step=1)
rooms = st.number_input("Habitaciones", min_value=1, max_value=30, value=3, step=1)
latitude = st.number_input("Latitud", min_value=52, max_value=52.5, value=52.3702, step=0.01) 
longitude = st.number_input("Longitud", min_value=4.5, max_value=5.1, value=4.8952, step=0.01)  

if st.button("Predecir precio"):
    # Crear dataframe con los mismos nombres de columnas que en el entrenamiento
    input_data = pd.DataFrame([{
        "Area": area,
        "Room": rooms,
        "Lat": latitude,
        "Lon": longitude
    }])

    # Hacer predicción
    prediction = model.predict(input_data)[0]

    st.success(f"El precio estimado de la vivienda es: {prediction:,.2f}€")


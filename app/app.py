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
latitud = st.number_input("Latitud", min_value=52.0, max_value=52.5, value=52.3702, step=0.01, format="%.4f") 
longitud = st.number_input("Longitud", min_value=4.5, max_value=5.1, value=4.8952, step=0.01, format="%.4f")  

if st.button("Predecir precio"):
    # Crear dataframe con los mismos nombres de columnas que en el entrenamiento
    input_data = pd.DataFrame([{
        "Area": area,
        "Room": rooms,
        "Lon": longitud,
        "Lat": latitud
    }])

    # Hacer predicción
try:
    prediction = model.predict(input_data)[0]
    st.success(f"El precio estimado de la vivienda es: {prediction:,.2f}€")
except Exception as e:
    st.error(f"Ocurrió un error al predecir: {e}")

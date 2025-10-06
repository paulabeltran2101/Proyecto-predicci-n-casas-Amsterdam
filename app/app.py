import streamlit as st
import joblib
import pandas as pd
from PIL import Image

#---Configuración general---
st.set_page_config(
    page_title="Predicción de precios de la vivienda en Ámsterdam 🏡",
    page_icon="🏡",
    layout="centered"
)

#Fondo con imagen (enlace público)
background_url = "https://raw.githubusercontent.com/paulabeltran2101/Proyecto-predicci-n-casas-Amsterdam/main/images/amsterdam.jpg"

#CSS para fondo y estilo general
page_background = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

[data-testid="stHeader"], [data-testid="stToolbar"] {{
    background: rgba(0,0,0,0);
}}

div.block-container {{
    background: rgba(255, 255, 255, 0.95);
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}}

</style>
"""
st.markdown(page_background, unsafe_allow_html=True)

# Cargar modelo entrenado
model = joblib.load("model/best_model_rf.pkl")

st.title("🏡Predicción de precios de casas en Ámsterdam🏡")

st.write("Introduce las características de la vivienda para estimar su valor aproximado:")

# Inputs del usuario

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("📏 Área (m²)", min_value=10, max_value=1000, value=90, step=1)
    rooms = st.number_input("🛏️ Habitaciones", min_value=1, max_value=30, value=3, step=1)

with col2:
    latitud = st.number_input("🌍 Latitud", min_value=52.0, max_value=52.5, value=52.3702, step=0.01, format="%.4f")
    longitud = st.number_input("🧭 Longitud", min_value=4.5, max_value=5.1, value=4.8952, step=0.01, format="%.4f")

#Predicción

if st.button("💡Predecir precio"):
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
    st.success(f"💰El precio estimado de la vivienda es: {prediction:,.2f}€")
    st.balloons()
    
except Exception as e:
    st.error(f"Ocurrió un error al predecir: {e}")

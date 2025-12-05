import streamlit as st
from streamlit_extras.let_it_rain import rain
import requests

API_URL = "http://server:8000"

st.set_page_config(page_title="Fruit App", page_icon="🍎")
st.title("🍎 My Beautiful Fruit App")

# -------------------------
# Vérification API
# -------------------------
st.subheader("🔌 API Status")

try:
    r = requests.get(f"{API_URL}/")
    if r.status_code == 200:
        st.success("✅ API connected")
        st.write(r.json())
    else:
        st.error("❌ API not responding")
except:
    st.error("❌ Impossible de se connecter à l'API")

# -------------------------
# Ajouter un fruit
# -------------------------
st.subheader("➕ Add a fruit")

fruit = st.text_input("Nom du fruit")

if st.button("Ajouter"):
    if fruit:
        r = requests.get(f"{API_URL}/add/{fruit}")
        if r.status_code == 200:
            st.success("Fruit ajouté ✅")
            st.write(r.json())
            st.snow()
        else:
            st.error("Erreur lors de l'ajout")
    else:
        st.warning("Entre un nom de fruit.")

# -------------------------
# Liste des fruits
# -------------------------
st.subheader("📋 Liste des fruits")

if st.button("Afficher la liste"):
    r = requests.get(f"{API_URL}/list")
    if r.status_code == 200:
        fruits = r.json()
        st.write(fruits)
    else:
        st.error("Erreur lors de la récupération")
        

# -------------------------
# Prédiction Iris
# -------------------------
st.subheader("🌸 Prédiction d'une fleur")

sepal_length = st.number_input("Sepal length", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal width", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal length", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal width", min_value=0.0, step=0.1)

if st.button("Prédire"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    r = requests.post(f"{API_URL}/predict", json=data)

    if r.status_code == 200:
        st.success("✅ Fleur prédite")
        st.write(r.json())
        
        emoji_map = {
            "setosa": "🌺",
            "virginica": "🌼",
            "versicolor": "🌻",
        }
    prediction = r.json()["prediction"]
        
    emoji = emoji_map.get(prediction)

    if emoji:
        rain(
            emoji=emoji,
            font_size=54,
            falling_speed=5,
            animation_length="infinite",
        )
    else:
        st.error("❌ Erreur lors de la prédiction")
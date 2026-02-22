import streamlit as st
import joblib
import pandas as pd
import numpy as np

# -------------------------------
# Load Model
# -------------------------------
MODEL_PATH = "xgboost_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# -------------------------------
# Get Feature Names From Model
# -------------------------------
try:
    FEATURE_COLUMNS = model.get_booster().feature_names
except:
    FEATURE_COLUMNS = model.feature_names_in_

# -------------------------------
# Preprocessing Function
# -------------------------------
def preprocess_input(total_sqft, bath, bhk, location_input):
    
    x = pd.DataFrame(
        np.zeros((1, len(FEATURE_COLUMNS))),
        columns=FEATURE_COLUMNS
    )

    x["total_sqft"] = total_sqft
    x["bath"] = float(bath)
    x["bhk"] = float(bhk)

    if location_input != "other" and location_input in FEATURE_COLUMNS:
        x[location_input] = 1

    return x


# -------------------------------
# UI
# -------------------------------
st.title("🏡 Bangalore House Price Prediction")

with st.sidebar:
    st.header("House Details")

    total_sqft = st.slider("Total Square Feet", 300.0, 10000.0, 1200.0, 50.0)
    bath = st.slider("Number of Bathrooms", 1, 10, 2)
    bhk = st.slider("Number of BHK", 1, 10, 2)

    location_options = [
        col for col in FEATURE_COLUMNS
        if col not in ["total_sqft", "bath", "bhk"]
    ]

    location_list = sorted(location_options + ["other"])
    location = st.selectbox("Location", location_list)


# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price"):

    input_df = preprocess_input(total_sqft, bath, bhk, location)

    try:
        prediction = model.predict(input_df)[0]

        st.success(f"### Predicted Price: ₹ {prediction:.2f} Lakhs")
        st.info("Price is approximate and may vary with market conditions.")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
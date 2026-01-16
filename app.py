import streamlit as st
import pandas as pd
import numpy as np
import joblib
import gdown
import os
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Full page background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0b1220);
    color: white;
}

/* Title style */
.main-title {
    font-size: 45px;
    font-weight: 800;
    text-align: center;
    background: -webkit-linear-gradient(#38bdf8, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-top: -10px;
    margin-bottom: 25px;
}

/* Card style */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 18px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 4px 18px rgba(0,0,0,0.35);
    margin-bottom: 20px;
}

/* Prediction result */
.result-card {
    background: linear-gradient(135deg, rgba(56,189,248,0.25), rgba(167,139,250,0.25));
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.18);
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    margin-top: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.45);
}

/* Button styling */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #38bdf8, #a78bfa);
    color: white;
    border: none;
    padding: 12px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
    transition: 0.3s;
}
div.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 20px rgba(56,189,248,0.35);
}

/* Input labels */
label {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 30px;
    color: #94a3b8;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='main-title'>🚗 Used Car Price Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Enter car details and get an instant resale price estimate powered by ML</div>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 About this App")
st.sidebar.info(
    "This app predicts the resale value of a used car based on features like brand, year, mileage, fuel type, engine and more."
)
st.sidebar.markdown("---")
st.sidebar.write("🔹 Model: Random Forest")
st.sidebar.write("🔹 Output: Price in Lakhs (₹)")

# ---------------- LOAD MODEL ----------------

MODEL_PATH = "models/rf_used_car_price_model.pkl"
DRIVE_FILE_ID = "PASTE_YOUR_FILE_ID_HERE"
MODEL_URL = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"

def download_model():
    os.makedirs("models", exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        with st.spinner("📥 Downloading ML model... Please wait"):
            gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

download_model()
model = joblib.load(MODEL_PATH)


# ---------------- INPUT UI (CARDS + COLUMNS) ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

brand_list = [
    "Maruti", "Hyundai", "Honda", "Toyota", "Mahindra", "Tata",
    "Ford", "Volkswagen", "Renault", "Nissan", "Skoda", "Chevrolet",
    "BMW", "Audi", "Mercedes-Benz", "Kia", "Jeep", "Datsun",
    "Fiat", "Mitsubishi", "Volvo", "Jaguar", "Land Rover", "Mini",
    "Porsche", "ISUZU", "Lexus"
]

with col1:
    st.subheader("🧾 Car Identity")
    brand = st.selectbox("Brand Name", sorted(brand_list), index=0)

    
    model_name = st.text_input("Model Name", "Wagon R LXI CNG")
    location = st.selectbox(
        "Location",
        ["Mumbai", "Pune", "Chennai", "Coimbatore", "Delhi", "Hyderabad", "Kochi", "Kolkata", "Jaipur", "Ahmedabad"]
    )

with col2:
    st.subheader("📅 Usage Details")
    year = st.number_input("Year", min_value=1995, max_value=2020, value=2015)
    kms = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=50000)

st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<div class='card'>", unsafe_allow_html=True)

col3, col4, col5 = st.columns(3)

with col3:
    st.subheader("⛽ Fuel & Transmission")
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

with col4:
    st.subheader("👤 Ownership")
    owner_type = st.selectbox("Owner Type", ["First", "Second", "Third", "Fourth & Above"])
    seats = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9, 10], index=2)

with col5:
    st.subheader("⚙️ Technical Specs")
    mileage = st.number_input("Mileage (km/l)", min_value=0.0, max_value=50.0, value=18.0)
    engine = st.number_input("Engine (CC)", min_value=500.0, max_value=6000.0, value=1200.0)
    power = st.number_input("Power (bhp)", min_value=20.0, max_value=600.0, value=85.0)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- PREDICT ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📈 Prediction")

if st.button("Predict Price 🚀"):
    CURRENT_YEAR = 2020
    car_age = CURRENT_YEAR - year

    input_df = pd.DataFrame([{
        "Brand_Name": brand,
        "Model_Name": model_name,
        "Location": location,
        "Fuel_Type": fuel,
        "Transmission": transmission,
        "Owner_Type": {"First": 1, "Second": 2, "Third": 3, "Fourth & Above": 4}[owner_type],
        "Mileage": mileage,
        "Seats": float(seats),
        "Car_Age": car_age,
        "Kilometers_Driven_log": np.log1p(kms),
        "Engine_log": np.log1p(engine),
        "Power_log": np.log1p(power),
        "Power_per_CC": np.log1p(power) / np.log1p(engine)
    }])

    pred_price = model.predict(input_df)[0]

    st.markdown(
        f"<div class='result-card'>✅ Estimated Resale Price<br><span style='font-size:40px;'>₹ {pred_price:.2f} Lakhs</span></div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<div class='footer'>Built with ❤️ using Streamlit | Used Car Price Prediction ML App</div>", unsafe_allow_html=True)

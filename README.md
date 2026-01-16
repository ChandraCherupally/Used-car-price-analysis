# 🚗 Used Car Price Prediction (End-to-End ML + Streamlit Deployment)

A complete **machine learning project** that predicts the **resale price of used cars (₹ Lakhs)** based on key vehicle attributes like brand, model, year, mileage, engine, power, fuel type, transmission, and ownership.

✅ Includes: Data Cleaning → EDA → Feature Engineering → Model Training → Deployment

---

## 🌐 Live App (Streamlit Deployment)

🚀 **Try the app here:**  
👉 https://cars24-used-car-price-analysis.streamlit.app/

---

## 📌 Project Highlights

- Built an end-to-end ML pipeline for used car price prediction
- Cleaned and transformed raw data into model-ready format
- Performed EDA to identify key pricing drivers (age, mileage, power, brand)
- Trained and evaluated a **Random Forest Regression model**
- Deployed a fully functional **Streamlit web application** for real-time predictions

---

## 🖥️ Streamlit App Preview

The app allows users to input car details and instantly get the predicted resale price:

- Brand Name (dropdown)
- Model Name
- Location
- Year, Kilometers Driven
- Fuel Type, Transmission
- Owner Type, Seats
- Mileage, Engine (CC), Power (bhp)

---

## 📊 Model Performance (Random Forest Pipeline)

Final evaluation results:

- **MAE**  : **1.545**
- **RMSE** : **4.293**
- **R²**   : **0.862**

📌 Interpretation:
- Model explains **~86% of variance** in used car prices  
- Average prediction error is around **₹1.5 Lakhs**
- Performs well across common market cars; luxury/high-end cars may have higher deviations due to price volatility

---

## 🧹 Data Cleaning Summary

Key cleaning steps performed:
- Removed duplicates and handled missing values
- Converted mixed-type columns like `Mileage`, `Engine`, and `Power` into numeric format
- Standardized categorical columns (Fuel type, Transmission, Owner type, etc.)
- Validated outliers (luxury cars were treated as valid market cases)

---

## 📊 Exploratory Data Analysis (EDA) Insights

### 🔹 Numerical Insights
- **Newer cars consistently have higher prices**, showing strong impact of depreciation (Year)
- Most vehicles fall within **30k–80k km**, while very high-mileage cars are less common
- **Engine and Power strongly influence price**, separating budget vs premium segments
- Price distribution is **right-skewed** with a luxury tail

### 🔹 Categorical Insights
- **Diesel and Petrol dominate** the used car market
- **Manual transmission** is more common, while **Automatic** tends to have higher resale value
- **First-owner cars retain higher value**, price reduces as ownership count increases
- **Maruti and Hyundai** contribute most listings in the dataset

---

## ⚙️ Feature Engineering

Key engineered features used during training:
- **Car_Age = CurrentYear - Year**
- Log transforms:
  - `Kilometers_Driven_log = log1p(Kilometers_Driven)`
  - `Engine_log = log1p(Engine)`
  - `Power_log = log1p(Power)`
- Power efficiency:
  - `Power_per_CC = log1p(Power) / log1p(Engine)`
- Ordinal encoding:
  - `Owner_Type`: First < Second < Third < Fourth+

---

## 🤖 Model Training

### ✅ Best Model: Random Forest Regressor

Random Forest was selected because it:
- Captures non-linear relationships (Age vs Price, Power vs Price)
- Handles feature interactions well
- Performs strongly without heavy scaling requirements

---

## 🧠 Recommendations / Future Improvements

- Add **model explainability** using feature importance / SHAP
- Improve handling of high-cardinality text features like `Model_Name`
- Experiment with **XGBoost / LightGBM / CatBoost** for potentially better accuracy
- Add prediction intervals (min–max price range) for better user trust
- Store and serve model from a dedicated artifact store (HuggingFace/S3)

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
- **Matplotlib / Seaborn (EDA)**

---

## ▶️ How to Run Locally

### 1) Clone repository
```bash
git clone https://github.com/ChandraCherupally/Used-car-price-analysis.git
cd Used-car-price-analysis

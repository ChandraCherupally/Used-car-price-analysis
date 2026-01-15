## 🧹 Data Cleaning Summary
Key cleaning steps performed:
- Removed duplicates and handled missing values
- Converted mixed-type columns like `Mileage`, `Engine`, and `Power` into numeric format
- Standardized categorical columns (Fuel type, Transmission, Owner type, etc.)
- Checked and validated outliers (high-end cars were treated as valid market cases)

---

## 📊 Exploratory Data Analysis (EDA) Insights

### 🔹 Numerical Insights
- **Newer cars dominate listings**, indicating higher market demand for recent models.
- Most vehicles fall within **30k–80k km**, while very high-mileage cars are rare.
- **Price increases with Year**, confirming depreciation effect.
- **Engine and Power strongly influence Price**, separating mass-market and premium vehicles.
- Price distribution is **right-skewed**, with a small luxury tail.

### 🔹 Categorical Insights
- **Diesel and Petrol** dominate the used car market.
- **Manual transmission** is more common, but **automatic cars are priced higher**.
- **First-owner cars retain higher value**, and price drops with more owners.
- **Brand dominance:** Maruti and Hyundai contribute most listings.
- **Model dominance:** A few popular models account for most resale volume.

---

## 🧠 Recommendations
- Apply **log transformation** for skewed variables like Price and Kilometers Driven.
- Encode high-cardinality features (`Brand_Name`, `Model_Name`) using **frequency/target encoding**.
- Handle outliers carefully: luxury cars are **valid data points**, not noise.
- Use tree-based models (Random Forest / Gradient Boosting) for best non-linear performance.

---

## ⚙️ Feature Engineering
Key engineered features used for training:
- **Car_Age = CurrentYear - Year**
- Log transforms:
  - `log(Kilometers_Driven)`
  - `log(Engine)`
  - `log(Power)`
- Frequency encoding:
  - `Brand_Name_freq`
  - `Model_Name_freq`
- One-hot encoding:
  - Fuel type, transmission, seats
- Ordinal encoding:
  - Owner type (First < Second < Third < Fourth+)

---

## 🤖 Model Training & Results
### ✅ Best Model: Random Forest Regressor
Performance on test data:

| Model | RMSE | MAE | R² |
|------|------|-----|----|
| Random Forest | **4.474** | **1.640** | **0.850** |

📌 Interpretation:
- The model explains **85% of price variance**
- Predictions are generally stable with low average error
- High-end cars create some larger deviations, which is expected

---

## 🌐 Streamlit Web App
The project includes a Streamlit application where users can:
- Select car attributes (fuel, transmission, owner type, seats)
- Enter numerical inputs (age/year, km driven, engine, power)
- Get an instant predicted resale price

### ▶️ Run Streamlit App Locally
```bash
pip install -r requirements.txt
streamlit run app/app.py

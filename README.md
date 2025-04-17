# 💡 SmartPremium – Predict Insurance Premiums with ML

SmartPremium leverages **machine learning** to predict insurance premiums based on customer details like age, income, credit score, vehicle details, and health status. By analyzing various risk-related features, the model aims to enhance premium accuracy — benefiting both insurers and policyholders.

👉 **Live Demo**: [🌐 SmartPremium Web App](https://smartpremium-estimating-insurance-premiums-with-machine-learni.streamlit.app/)

---

## 🚀 Features

### ✅ Data Preprocessing & Feature Engineering
- Handling missing values
- Encoding categorical variables
- Log transformation of skewed features
- Feature scaling with `StandardScaler`

### 🤖 Machine Learning Models Implemented
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- **XGBoost Regressor** (Selected Best)

### 📊 Model Evaluation Metrics
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score (Coefficient of Determination)
- RMSLE (Root Mean Squared Log Error)

### ✅ MLflow Integration for Model Tracking
- Logs hyperparameters, metrics, and trained models
- Enables comparison of different models

### 🌐 Streamlit UI for Predictions
- Enter individual customer details to get real-time insurance premium prediction
- Built-in feature scaling and transformation before prediction

---

## 🗂 Folder Structure

```
SmartPremium/
│
├── Data Cleaning.ipynb
├── Data Preprocessing.ipynb
├── Data Modelling.ipynb
├── EDA.ipynb
├── Test data.ipynb
│
├── streamlit.py                ← Streamlit App
├── requirements.txt            ← Python dependencies
├── xgb_model.pkl               ← Best trained model
├── scaler.pkl                  ← StandardScaler for preprocessing
├── Logo.ipng                   ← App logo
├── README.md
```

---

## 📌 Model Training & Optimization

### 1️⃣ Data Preprocessing
- Missing value handling
- Categorical encoding
- Log transformation
- Feature scaling with `StandardScaler`

### 2️⃣ Model Training
- Multiple models tested
- Evaluation: RMSE, MAE, R² Score, RMSLE

### 3️⃣ Model Selection & Saving
- **XGBoost** selected as best-performing model
- Saved as `xgb_model.pkl`  
- Scaler saved as `scaler.pkl`

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Someshwaran46/SmartPremium-Estimating-Insurance-Premiums-with-Machine-Learning.git
cd SmartPremium-Estimating-Insurance-Premiums-with-Machine-Learning
```

### 2️⃣ Create & Activate Virtual Environment

#### 🪟 Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ View MLflow Model Metrics (Optional)

```bash
mlflow ui 
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) to explore:
- Model runs
- Parameters
- Evaluation metrics

---

### 6️⃣ Run the Streamlit UI

```bash
streamlit run streamlit.py
```

You can:
- Enter customer details manually  
- Or upload CSV files for bulk predictions

---

## 📬 Feedback

Feel free to open issues or submit pull requests! Improvements, and suggestions are always welcome 🙌

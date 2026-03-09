## 📌 Project Overview

This project is a Machine Learning–based web application that predicts house prices in Bangalore based on various real estate features such as location, size, total square feet, number of bathrooms, and balconies.

The model is trained using regression algorithms and deployed using Streamlit, allowing users to input property details and get real-time price predictions.

---

## 🎯 Problem Statement

Real estate pricing in Bangalore varies significantly depending on location and property features. Buyers and sellers often struggle to estimate fair property prices.

The objective of this project is to develop a regression model that accurately predicts house prices based on historical housing data.

---

## 📊 Dataset Description

The dataset contains property listings from Bangalore and includes features such as:

* Location
* Total Square Feet
* Number of Bedrooms (BHK)
* Number of Bathrooms
* Number of Balconies
* Price (Target Variable)

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Handling missing values
* Removing outliers
* Converting categorical variables (Location) using One-Hot Encoding
* Feature Engineering (Extracting BHK from size column)
* Normalizing numerical features

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Cleaning

Removed invalid entries and outliers.

### 2️⃣ Feature Engineering

Created meaningful features from raw data.

### 3️⃣ Encoding

Applied One-Hot Encoding to location column.

### 4️⃣ Train-Test Split

* 80% Training Data
* 20% Testing Data

### 5️⃣ Model Training

Regression algorithms used:

* Linear Regression
* Lasso Regression
* Decision Tree Regressor

### 6️⃣ Model Evaluation

Performance evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

### 7️⃣ Model Saving

Best performing model saved using Pickle as:

```
linear_regression_model.pkl
xgboost_model.pkl
```

---

## 🚀 Features of the Application

✅ User-friendly Streamlit interface
✅ Real-time house price prediction
✅ Location-based pricing
✅ Model comparison
✅ Cleaned and preprocessed dataset
✅ Saved trained model

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Pickle

---

## 📂 Project Structure

```
├── app.py
├── bangalore_house_prices.csv
├── bangalore_house_price_model.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```
gh repo clone sachinsharma19112003/bangalore-house-price
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Application

```
streamlit run app.py
```

---

## 📈 Model Performance

The regression model achieved strong predictive performance with high R² score, indicating good accuracy in estimating house prices.

Performance metrics ensure reliability for real-world usage scenarios.

---

## 🌐 Deployment

The application can be deployed on: https://bangalore-house-price-rvn27hxuhrxxfbnmvqxoue.streamlit.app/

* Streamlit Cloud

## 👨‍💻 Author

Sachin Sharma
Machine Learning Enthusiast | Data Scientist 



# 🏦 Banking Loan Default Prediction App

A Flask-based Machine Learning web application that predicts whether a customer is at risk of defaulting on a loan based on their financial information.

## 🚀 Live Demo

Live Application: https://banking-app-flask.onrender.com

## 📌 Project Overview

This project uses a trained Random Forest Machine Learning model to predict loan default risk based on customer financial attributes.

Users enter:

* Employment Years
* Income
* Debt-to-Income Ratio
* Credit Debt
* Other Debt

The application then predicts whether the customer has:

* ✅ Low Risk of Default
* ⚠️ High Risk of Default

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* Random Forest Classifier
* HTML
* Bootstrap 5
* Render (Deployment)

## 📂 Project Structure

```text
Banking Application Model
│
├── application.py
├── RF_model_exaple.pkl
├── requirements.txt
├── Procfile
│
├── templates
│   └── index.html
│
└── static
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Adi46878/banking-app-flask.git
cd banking-app-flask
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python application.py
```

Open:

```text
http://127.0.0.1:5000
```

## 🧠 Machine Learning Model

The prediction model was trained using a Random Forest Classifier on banking loan data.

### Input Features

| Feature  | Description          |
| -------- | -------------------- |
| employ   | Employment Years     |
| income   | Annual Income        |
| debtinc  | Debt-to-Income Ratio |
| creddebt | Credit Debt          |
| othdebt  | Other Debt           |

### Output

* 0 → Low Risk of Default
* 1 → High Risk of Default

## 📸 Application Features

* Modern Bootstrap UI
* Real-time Loan Risk Prediction
* Responsive Design
* Flask Backend Integration
* Machine Learning Inference

## 🌐 Deployment

The application is deployed using Render and automatically updates whenever new changes are pushed to GitHub.

## 👨‍💻 Author

**Aditya**

GitHub: https://github.com/Adi46878

```
```

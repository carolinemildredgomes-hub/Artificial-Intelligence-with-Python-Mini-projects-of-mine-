# Dropshipping Success Predictor using Machine Learning

## Overview

The **Dropshipping Success Predictor** is a machine learning project that predicts whether a dropshipping product is likely to receive **high customer ratings (4–5 stars)** or **low customer ratings (1–3 stars)** based on product, supplier, shipping, and marketing information.

This project demonstrates the complete machine learning workflow, including data preprocessing, feature encoding, model training, prediction, and evaluation using a **K-Nearest Neighbors (KNN)** classifier.

---

## Problem Statement

Choosing profitable products is one of the biggest challenges in a dropshipping business.

Instead of relying solely on experience, this project uses historical product information to train a machine learning model that predicts whether a product is likely to receive positive customer ratings.

Such predictions can help business owners prioritize products with higher customer satisfaction potential.

---

## Features Used

The model is trained using the following features:

* Product Price
* Shipping Days
* Supplier Rating
* Number of Customer Reviews
* Refund Rate
* Free Shipping
* Express Delivery
* Marketing Budget
* Advertising Platform
* Product Category

### Target Variable

**HighRating**

* `1` → High Rating (4–5 stars)
* `0` → Low Rating (1–3 stars)

---

## Machine Learning Algorithm

This project uses the **K-Nearest Neighbors (KNN)** classification algorithm.

Configuration:

* Algorithm: K-Nearest Neighbors
* Number of Neighbors (`k`): 1
* Library: Scikit-learn

---

## Workflow

1. Load the CSV dataset.
2. Convert categorical values into numerical values.
3. Separate evidence and labels.
4. Split the dataset into training and testing sets.
5. Train the KNN model.
6. Predict customer ratings for unseen products.
7. Evaluate the model using classification metrics.

---

## Feature Encoding

Categorical values are converted into integers before training.

### Advertising Platform

* Facebook → 0
* Instagram → 1
* TikTok → 2
* Google → 3
* Pinterest → 4

### Product Category

* Electronics → 0
* Fashion → 1
* Home → 2
* Beauty → 3
* Sports → 4
* Pets → 5
* Books → 6

### Boolean Values

* TRUE → 1
* FALSE → 0

---

## Evaluation Metrics

The model is evaluated using:

* Accuracy
* Sensitivity (True Positive Rate)
* Specificity (True Negative Rate)
* Precision
* Recall
* F1 Score
* Confusion Matrix

These metrics provide a comprehensive understanding of the classifier's performance.

---

## Technologies Used

* Python
* Scikit-learn
* CSV
* NumPy (optional)
* Pandas (optional)

---

## Learning Outcomes

This project helped me understand:

* Data preprocessing
* Feature engineering
* K-Nearest Neighbors classification
* Model training and prediction
* Binary classification
* Model evaluation techniques
* Building complete machine learning pipelines

---

## Future Improvements

Potential enhancements include:

* Support Vector Machine (SVM)
* Random Forest Classifier
* Decision Tree Classifier
* Logistic Regression
* Hyperparameter tuning
* Cross-validation
* Feature importance analysis
* Interactive dashboard using Streamlit

---

## Project Structure

```text
dropshipping-success-predictor/
│── data/
│   └── dropshipping.csv
│── model.py
│── README.md
│── requirements.txt
│── screenshots/
└── LICENSE
```

---

## Author

**Caroline Mildred Gomes**

English Literature Student | AI & Python Learner

Passionate about Artificial Intelligence, Machine Learning, Data Analytics, Software Development, and building practical AI applications.

GitHub: https://github.com/carolinemildredgomes-hub

---

## License

This project is intended for educational and portfolio purposes.

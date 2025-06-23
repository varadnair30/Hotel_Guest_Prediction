# Hotel_Guest_Prediction

![image](https://github.com/user-attachments/assets/2c9977c0-ea75-446b-8968-5845726cf8e6)


# Introduction -Link: https://hotel-1015024842965.us-central1.run.app/

The hospitality industry faces a significant challenge with booking cancellations, which can lead to revenue loss, operational inefficiencies, and planning difficulties. Understanding and predicting customer cancellation behavior has thus become crucial for optimizing hotel management strategies and enhancing guest satisfaction.

The project adopts a structured approach, encompassing data exploration, feature engineering, model development, model evaluation, and deployment. Furthermore, the solution is enhanced through the integration of MLOps tools such as MLflow for experiment tracking, Docker for containerization, and Google Cloud Platform for model hosting. Interactive visualizations built with Tableau provide stakeholders with intuitive insights into customer behaviors and booking trends.

# Dataset Overview

-Dataset Link: https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset

Dataset Size: 29,020 rows, 18 columns

Features: - Booking_ID, Number of Adults, Children, Number of Week/Weekend Nights, Meal Plan Type, Car Parking Requirement, Room Type Reserved, Lead Time, Arrival Date Details, Market Segment Type, Repeated Guest Flag, Previous Cancellation Count, Previous Bookings Not Canceled, Average Price Per Room , Special Requests, Booking Status (Target)

# Data preprocessing

-EDA

- Handling Imbalance Data with SMOTE

- Standardisation

# Tableau

-Link:  

![image](https://github.com/user-attachments/assets/a6bd37b6-3f7d-4297-91fc-280b07143256)


# ML Models

![image](https://github.com/user-attachments/assets/b662ed6e-d14f-41f2-838a-91597d33adfa)

Randomized Search CV for Hyper parameter tuning

For deployment LightGBM is used

# Model Architecture

Stages:

● Data Ingestion: Load and clean raw data

● Data Preprocessing: Encode, normalize, and apply SMOTE

● Model Training: Train models, evaluate performance

● Model Evaluation: Selecting the best model using cross-validation

● Model Saving: Save using joblib for future use.

Below is the model architecture:

1) Model- LightGBM

2)MLFLOW for model registering

3)GitHub for code Versioning

4)Docker for contanerisation

5)Jenkins for Continuous Integration/ Continuous Delivery

6)Google Cloud Platform for Deployment

7)HTML, CSS, and Flask for building the web application

![image](https://github.com/user-attachments/assets/5ebb3306-dd3f-47e1-acb9-0838c2c6dd1c)

![image](https://github.com/user-attachments/assets/bfe3bcc3-6ee2-4fd4-a22c-69d6bfb20f58)

Precision of 91% as shown in MLFLOW

# Friendly Interface

-Link: https://hotel-1015024842965.us-central1.run.app/

![image](https://github.com/user-attachments/assets/f748c663-768e-4dba-b956-eb2e9426a6e7)

![image](https://github.com/user-attachments/assets/b8d9c6b6-0411-4428-b1c6-a38611a71efb)


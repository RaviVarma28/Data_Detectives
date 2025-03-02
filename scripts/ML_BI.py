# If you want to integrate the dataset directly to PowerBI,
# a dataset was created with suffix 'Predictions' in the data folder in the repo.

# or you Copy the below script into the PowerBI run python script to predict the profit for the whole dataset
# Make sure permissions were given in the PowerBI

import pandas as pd
import joblib


model_path = "insert the file path/ml_model.pkl" # Insert the model file path

dataset = dataset

# The derived feature
dataset['Cost per Flight Hour'] = dataset['Operating Cost (USD)'] / dataset['Aircraft Utilization (Hours/Day)']

# Loading the model
xgb_model = joblib.load(model_path)

# Predicting the Target (Profit (USD))
features = ['Cost per ASK', 'Cost per Flight Hour', 'Revenue per ASK', 'Fuel Efficiency (ASK)']
dataset["Predicted Profit"] = xgb_model.predict(dataset[features])

dataset # This will be taken by PowerBI as input
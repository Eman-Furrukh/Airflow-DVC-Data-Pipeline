import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load the processed data
data = pd.read_csv('processed_data.csv')

# Features and target
X = data[['Humidity', 'Wind Speed']]  # You can add 'Weather Condition' after encoding if needed
y = data['Temperature']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")

predicted_temps = model.predict(X)
print(f"Predicted Temperatures: {predicted_temps[:5]}")

# Evaluate model performance
mse = mean_squared_error(y, predicted_temps)
r2 = r2_score(y, predicted_temps)

print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
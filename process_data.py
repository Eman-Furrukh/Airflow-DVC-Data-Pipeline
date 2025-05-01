import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load raw data
df = pd.read_csv("raw_data.csv")

# Handle missing values (drop rows with missing data)
df.dropna(inplace=True)

# Normalize temperature and wind speed
scaler = MinMaxScaler()
df[['Temperature', 'Wind Speed']] = scaler.fit_transform(df[['Temperature', 'Wind Speed']])

# Save the processed data
df.to_csv("processed_data.csv", index=False)
print("Preprocessing complete. Saved to 'processed_data.csv'")

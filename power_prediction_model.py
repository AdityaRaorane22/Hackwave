import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load data from CSV file
data = pd.read_excel('u2020.xlsx')
data.csv('output.csv',index=False)

# Extract features and target variable
X = data[['air_temperature', 'pressure', 'wind_speed']]
y = data['power_consumption']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Save the model
joblib.dump(model, 'power_prediction_model.pkl')

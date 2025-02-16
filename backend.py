from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('power_prediction_model.pkl')

# Prediction route
@app.route('/predict_power', methods=['POST'])
def predict_power():
    data = request.get_json()
    air_temperature = data['air_temperature']
    pressure = data['pressure']
    wind_speed = data['wind_speed']
    prediction = model.predict([[air_temperature, pressure, wind_speed]])
    return jsonify({'predicted_power': prediction[0]})

# Distribution route
@app.route('/distribute_power', methods=['POST'])
def distribute_power():
    data = request.get_json()
    predicted_power = data['predicted_power']
    node1_power = predicted_power * 0.20
    node2_power = predicted_power * 0.35
    node3_power = predicted_power * 0.45
    return jsonify({'node1_power': node1_power, 'node2_power': node2_power, 'node3_power': node3_power})

if __name__ == '__main__':
    app.run(debug=True)

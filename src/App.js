import React, { useState } from 'react';
import axios from 'axios'; // Import axios for API requests
import './App.css'; // Import CSS file for styling

function App() {
  const [temperature, setTemperature] = useState('');
  const [windSpeed, setWindSpeed] = useState('');
  const [pressure, setPressure] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handlePredictClick = async () => {
    try {
      const response = await axios.post('/predict', {
        temperature: temperature,
        wind_speed: windSpeed,
        pressure: pressure
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error predicting power generation:', error);
    }
  };

  return (
    <div className="App">
      <h1 className="title">Power Generation Prediction</h1>
      <div className="input-container">
        <label className="input-label">
          Air Temperature:
          <input className="input-field" type="number" value={temperature} onChange={e => setTemperature(e.target.value)} />
        </label>
        <br />
        <label className="input-label">
          Wind Speed:
          <input className="input-field" type="number" value={windSpeed} onChange={e => setWindSpeed(e.target.value)} />
        </label>
        <br />
        <label className="input-label">
          Pressure:
          <input className="input-field" type="number" value={pressure} onChange={e => setPressure(e.target.value)} />
        </label>
        <br />
        <button className="predict-button" onClick={handlePredictClick}>Predict Power Generation</button>
      </div>
      {prediction !== null && (
        <div className="prediction-container">
          <h2 className="prediction-text">Predicted Power Generation: {prediction} MW</h2>
        </div>
      )}
    </div>
  );
}

export default App;

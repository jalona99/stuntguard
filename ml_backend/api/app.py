from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
CORS(app)

# Load the trained model (placeholder - will be replaced with actual model)
# model = joblib.load('model/stuntguard_model.pkl')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract features
        age_months = data['age_months']
        gender_encoded = 1 if data['gender'].lower() == 'male' else 0
        birth_weight_kg = data['birth_weight_kg']
        height_cm = data['height_cm']
        weight_kg = data['weight_kg']

        # Prepare features array
        features = np.array([[age_months, gender_encoded, birth_weight_kg, height_cm, weight_kg]])

        # Placeholder prediction (replace with actual model)
        # prediction = model.predict(features)[0]
        # confidence = max(model.predict_proba(features)[0])

        # Mock prediction for now
        prediction = 'normal'  # normal, at_risk, stunted
        confidence = 0.95

        # Determine alert level
        alert_levels = {
            'normal': 'green',
            'at_risk': 'yellow',
            'stunted': 'red'
        }

        guidance_messages = {
            'normal': 'Child growth is within normal range. Continue monitoring.',
            'at_risk': 'Child shows signs of potential stunting risk. Consult healthcare provider.',
            'stunted': 'Child shows signs of stunting. Immediate medical attention recommended.'
        }

        response = {
            'classification': prediction,
            'confidence': confidence,
            'alert_level': alert_levels[prediction],
            'guidance': guidance_messages[prediction]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
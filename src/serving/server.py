from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('/models/iris_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    prediction = model.predict([input_data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

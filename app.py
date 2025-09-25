from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
from PIL import Image
import random  # for simulating healthy/diseased leaf

# Create Flask app
app = Flask(__name__)
CORS(app)  # allow frontend (HTML) to talk to this backend

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    # Convert base64 image to PIL Image
    image_data = data['image'].split(",")[1]
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))

    # Simulate prediction
    if random.random() < 0.5:
        prediction = {
            "label": "Healthy Leaf",
            "confidence": round(random.uniform(85, 99), 1)
        }
    else:
        prediction = {
            "label": "Diseased Leaf",
            "confidence": round(random.uniform(70, 95), 1)
        }

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, render_template, jsonify
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os

app = Flask(__name__, template_folder='templates')

# Load your trained model
model = load_model(os.path.join(os.path.dirname(__file__), "mnist_model.h5"))

def predict_digit(img_array):
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=-1)
    return predicted_class[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    img_path = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file:
            # Save the uploaded image in the 'static' folder
            static_folder = os.path.join(app.root_path, 'static')
            filepath = os.path.join(static_folder, 'uploaded_image.png')
            file.save(filepath)
            
            # Predict the digit
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (28, 28))
            img = 255 - img  # Invert colors
            img = img / 255.0  # Normalize
            img_array = np.expand_dims(img, axis=0)  # Shape (1, 28, 28)
            img_array = np.expand_dims(img_array, axis=-1)  # Shape (1, 28, 28, 1)

            prediction = predict_digit(img_array)
            img_path = 'static/uploaded_image.png'  # Path to display in HTML
            img_path = img_path.replace('\\', '/')  # Ensure path is correct for URLs

    return render_template('index.html', prediction=prediction, img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)
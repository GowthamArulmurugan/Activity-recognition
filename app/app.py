from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
from model import load_model, predict_video

app = Flask(__name__)

# Load the model
model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['video']
    video_path = 'uploaded_video.mp4'
    file.save(video_path)

    # Predict the video
    prediction = predict_video(model, video_path)

    return jsonify({'predicted_class': prediction})

if __name__ == '__main__':
    app.run(debug=True)

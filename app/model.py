import tensorflow as tf
import numpy as np
import cv2

def load_model():
    # Load the pre-trained LRCN model
    return tf.keras.models.load_model('model/LRCN_model.h5')

def extract_frames(video_path, sequence_length=30, image_size=(64, 64)):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while len(frames) < sequence_length and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, image_size)
        frames.append(frame)

    while len(frames) < sequence_length:
        frames.append(np.zeros_like(frames[0]))  # Padding with zero frames

    cap.release()
    return np.array(frames)

def predict_video(model, video_path):
    frames = extract_frames(video_path)
    frames = np.expand_dims(frames, axis=0)  # Add batch dimension
    prediction = model.predict(frames)
    return np.argmax(prediction, axis=1)[0]  # Return the class index

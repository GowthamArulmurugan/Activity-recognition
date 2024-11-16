import cv2
import numpy as np

def preprocess_video(video_path, sequence_length=30, image_size=(64, 64)):
    # This function extracts frames from the video and resizes them
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

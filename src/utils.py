def load_model(model_path):
    import joblib
    model = joblib.load(model_path)
    return model

def preprocess_frame(frame):
    import cv2
    # Resize the frame to the size expected by the model
    frame = cv2.resize(frame, (64, 64))
    # Convert the frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Normalize the pixel values
    frame = frame / 255.0
    # Reshape the frame for the model
    frame = frame.reshape(1, 64, 64, 1)
    return frame
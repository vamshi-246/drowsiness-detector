class DrowsinessDetector:
    def __init__(self, model):
        self.model = model

    def detect_drowsiness(self, frame):
        processed_frame = self.preprocess_frame(frame)
        prediction = self.model.predict(processed_frame)
        return prediction

    def alert_user(self, is_drowsy):
        if is_drowsy:
            print("Alert: Drowsiness detected! Please take a break.") 

    def preprocess_frame(self, frame):
        # Implement preprocessing steps such as resizing, normalization, etc.
        return frame  # Placeholder for actual preprocessing logic
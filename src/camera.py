class Camera:
    def __init__(self):
        self.video_capture = None

    def start_camera(self):
        self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            raise Exception("Could not open video device")

    def get_frame(self):
        ret, frame = self.video_capture.read()
        if not ret:
            raise Exception("Could not read frame from video device")
        return frame

    def release_camera(self):
        if self.video_capture is not None:
            self.video_capture.release()
import cv2
import time
import winsound
import threading
import mediapipe as mp

# Alert sound function
def alert_user():
    print("ALERT TRIGGERED")
    threading.Thread(
        target=winsound.PlaySound,
        args=('alert.wav', winsound.SND_FILENAME | winsound.SND_ASYNC),
        daemon=True
    ).start()

# Initialize Mediapipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Eye landmark indices for EAR calculation (right and left eyes)
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
LEFT_EYE = [362, 385, 387, 263, 373, 380]

# EAR calculation
import math
def euclidean(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def calculate_ear(eye_points):
    A = euclidean(eye_points[1], eye_points[5])
    B = euclidean(eye_points[2], eye_points[4])
    C = euclidean(eye_points[0], eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear

def main():
    cap = cv2.VideoCapture(0)
    closed_eyes_frames = 0
    threshold_frames = 20
    alert_playing = False
    EAR_THRESHOLD = 0.21

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                height, width, _ = frame.shape
                landmarks = [(int(p.x * width), int(p.y * height)) for p in face_landmarks.landmark]

                right_eye = [landmarks[i] for i in RIGHT_EYE]
                left_eye = [landmarks[i] for i in LEFT_EYE]

                right_ear = calculate_ear(right_eye)
                left_ear = calculate_ear(left_eye)
                avg_ear = (right_ear + left_ear) / 2.0

                if avg_ear < EAR_THRESHOLD:
                    closed_eyes_frames += 1
                else:
                    closed_eyes_frames = 0
                    alert_playing = False

                for (x, y) in right_eye + left_eye:
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

                if closed_eyes_frames > threshold_frames:
                    cv2.putText(frame, "DROWSINESS ALERT!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    if not alert_playing:
                        alert_user()
                        alert_playing = True
                break  # Only process the first detected face

        cv2.imshow('Improved Drowsiness Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

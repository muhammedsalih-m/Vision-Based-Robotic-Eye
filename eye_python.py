import cv2
import serial
import time
import mediapipe as mp

# =============================================
# SERIAL COMMUNICATION
# =============================================
arduino = serial.Serial('COM3', 115200)   # Change COM port
time.sleep(4)

# =============================================
# MEDIAPIPE FACE MESH INITIALIZATION
# =============================================
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# =============================================
# HELPER: Calculate Eye Aspect Ratio (Blink Detection)
# =============================================
import math
def distance(a, b):
    return math.dist([a.x, a.y], [b.x, b.y])

def eye_aspect_ratio(landmarks, idx):
    # Eye landmarks indices for blink detection
    top = landmarks[idx[1]]
    bottom = landmarks[idx[5]]
    left = landmarks[idx[0]]
    right = landmarks[idx[3]]

    vertical = distance(top, bottom)
    horizontal = distance(left, right)
    return vertical / horizontal

# Mediapipe landmark indices for eye
RIGHT_EYE = [33, 159, 145, 133, 153, 144]
LEFT_EYE  = [362, 386, 374, 263, 380, 373]

# =============================================
# CAMERA LOOP
# =============================================
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # Convert to RGB for mediapipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        mesh = results.multi_face_landmarks[0].landmark

        # =============================================
        # FACE POSITION FOR EYEBALL MOVEMENT
        # =============================================
        nose = mesh[1]
        x = nose.x * w
        y = nose.y * h

        # Determine direction
        if x < w * 0.40:
            eye_dir = "LEFT"
        elif x > w * 0.60:
            eye_dir = "RIGHT"
        else:
            eye_dir = "CENTER"

        if y < h * 0.40:
            eye_vert = "UP"
        elif y > h * 0.60:
            eye_vert = "DOWN"
        else:
            eye_vert = "CENTER"

        # =============================================
        # BLINK DETECTION
        # =============================================
        ear_left = eye_aspect_ratio(mesh, LEFT_EYE)
        ear_right = eye_aspect_ratio(mesh, RIGHT_EYE)

        EAR = (ear_left + ear_right) / 2

        blink = EAR < 0.20   # threshold

        # =============================================
        # SEND COMMANDS TO ARDUINO
        # =============================================
        command = f"{eye_dir},{eye_vert},{int(blink)}\n"
        print("Sending:", command)
        arduino.write(command.encode())

    cv2.imshow("Animatronic Eye Control", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

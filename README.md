# Vision-Based-Robotic-Eye



👁️ Vision Based Animatronic Eye
📌 Project Overview

The Vision Based Animatronic Eye is a robotics and computer vision project that mimics human eye movement.
The system detects a human face using a camera and automatically moves an animatronic eye mechanism to follow the face in real time.

This project combines computer vision, embedded systems, and servo motor control to create a realistic robotic eye that can track a user and perform blinking actions.

🎯 Aim

To design and implement a vision-based animatronic eye system that detects a human face and mimics natural human eye movement.

⚙️ Hardware Components
No	Component	Quantity
1	SG90 Servo Motor	6
2	Arduino Uno	1
3	Sensor Shield v5	1
4	Camera Module / Webcam	1
5	Battery	1
🧠 Technologies Used

Python
OpenCV
MediaPipe Face Mesh
Arduino
Serial Communication
Servo Motor Control


Libraries used:
opencv-python
mediapipe
pyserial
time
math

🏗️ System Architecture

Camera captures real-time video.

Python program processes video using face detection.

The nose landmark position determines face direction.

Blink detection is performed using Eye Aspect Ratio (EAR).

Commands are sent to Arduino via serial communication.

Arduino controls 6 servo motors to move the animatronic eye.


🔄 Algorithm

Start the system.

Initialize servo motors at 90° neutral position.

Start the camera and face detection model.

Detect face landmarks using MediaPipe.

Extract the x and y position of the face.

Compare face position with camera center.

Move servo motors to simulate eye movement.

Detect blinking using Eye Aspect Ratio.

Send commands to Arduino.

Repeat continuously for real-time tracking.

👁️ Features

✔ Real-time face detection
✔ Eye movement tracking (Left / Right / Up / Down)
✔ Automatic blinking detection
✔ Smooth servo motor control
✔ Human-like animatronic eye behavior

🔌 Circuit Connections
Servo	Arduino Pin
Right Upper Eyelid	3
Right Lower Eyelid	5
Left Upper Eyelid	6
Left Lower Eyelid	9
Eyeball Horizontal	10
Eyeball Vertical	11


💻 Software Setup

Install required Python libraries:

pip install opencv-python mediapipe pyserial

Connect Arduino and update the correct COM port in the Python code.

Example:

arduino = serial.Serial('COM5', 115200)
▶️ Running the Project

Upload the Arduino code to the Arduino Uno.

Connect servo motors and camera.

Run the Python script:

python animatic_eye.py

The animatronic eye will start tracking the user's face.

📂 Project Structure
animatronic-eye
│
├── python_code/
│   └── animatic_eye.py
│
├── arduino_code/
│   └── eye_control.ino
│
├── circuit_diagram/
│
└── README.md

#include <Servo.h>

Servo rightUp;
Servo rightDown;
Servo leftUp;
Servo leftDown;
Servo eyeballH;
Servo eyeballV;

void setup() {
  Serial.begin(115200);

  rightUp.attach(3);
  rightDown.attach(5);
  leftUp.attach(6);
  leftDown.attach(9);
  eyeballH.attach(10);
  eyeballV.attach(11);

  centerEye();
}

void centerEye() {
  eyeballH.write(90);
  eyeballV.write(90);

  rightUp.write(90);
  rightDown.write(90);
  leftUp.write(90);
  leftDown.write(90);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');

    data.trim();
    int c1 = data.indexOf(',');
    int c2 = data.indexOf(',', c1 + 1);

    String horizontal = data.substring(0, c1);
    String vertical = data.substring(c1 + 1, c2);
    int blink = data.substring(c2 + 1).toInt();

    // ======================
    // EYEBALL MOVEMENT
    // ======================
    if (horizontal == "LEFT") eyeballH.write(120);
    else if (horizontal == "RIGHT") eyeballH.write(60);
    else eyeballH.write(90);

    if (vertical == "UP") eyeballV.write(120);
    else if (vertical == "DOWN") eyeballV.write(60);
    else eyeballV.write(90);

    // ======================
    // BLINK / EYELIDS
    // ======================
    if (blink == 1) {
      // Closed eyes
      rightUp.write(90);
      rightDown.write(90);
      leftUp.write(90);
      leftDown.write(90);
    } else {
      // Open eyes
      rightUp.write(140);
      rightDown.write(50);
      leftUp.write(40);
      leftDown.write(130);
    }
  }
}

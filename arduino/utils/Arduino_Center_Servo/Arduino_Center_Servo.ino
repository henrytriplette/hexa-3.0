#include <Servo.h>

Servo servo;  // Create servo object to control a servo

int centerValue = 90;   // Almost all standard servos have positions from 0 to 180 degrees, making 
                        // 90 the center point.

void setup() {
  servo.attach(3);  // Attaches the servo on pin 2 to the servo object
}

void loop() {
  servo.write(centerValue);          // Sets the servo position according to the center value above
  delay(100);                           // Waits for the servo to get there
}


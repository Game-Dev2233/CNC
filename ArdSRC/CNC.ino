#include <arduino.h>
const int ledPin = 12;  // Define the digital output pin

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);  // Set the digital output pin as an output
}

void loop() {
  if (Serial.available() > 0) {
    // Discard the incoming byte
    Serial.read();
    digitalWrite(12, HIGH);
  }
}

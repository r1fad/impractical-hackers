//const int analogInPin = A4;  // Analog input pin that the potentiometer is attached to
//int sensorValue = 0;        // value read from the pot
// 
//void setup() {
//  // initialize serial communications at 9600 bps:
//  Serial.begin(9600);
//  pinMode(9, INPUT_PULLUP); 
//}
// 
//void loop() {
//  // read the analog in value:
//  sensorValue = analogRead(analogInPin);              
//  // print the results to the serial monitor:
//  Serial.print("sensor = " );                       
//  Serial.println(sensorValue); 
//}


#include<Servo.h>

#define TURN_TIME 100

Servo someServo;

bool badPosture = true;

void setup() 
{
   
}  

void loop()
{

    if (badPosture) {
      someServo.attach(9);
      someServo.write(180);
      // Go on turning for the right duration
      delay(TURN_TIME);
      // Stop turning
      someServo.write(90);
      
      delay(2000);
      someServo.attach(9);
      someServo.write(0);
      delay(TURN_TIME);
      someServo.write(90);
      someServo.detach();
      badPosture = false;
    }

}

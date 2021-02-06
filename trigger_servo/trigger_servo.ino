const int pressureSensor = A4;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0;        // value read from the pot
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

Servo smacker;

bool badPosture = false;
bool procrastination = false;


void setup() {

  Serial.begin(9600);
  pinMode(pressureSensor, INPUT_PULLUP); 
   
}  

void loop() {

    sensorValue = analogRead(pressureSensor);              
    // print the results to the serial monitor:                      
    Serial.println(sensorValue); 

    if (badPosture || procrastination) {
      smackUser();
      badPosture = false;
      procrastination = false;
    }

}

void smackUser() {

    for (int i = 0; i <= 3; i++){
        smacker.attach(9);
        smacker.write(180);
        // Go on turning for the right duration
        delay(TURN_TIME);
        // Stop turning
        smacker.write(90);
        delay(2000);
        smacker.attach(9);
        smacker.write(0);
        delay(TURN_TIME);
        smacker.write(90);
        smacker.detach();    
    }
      
 }

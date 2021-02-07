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

#define DOWN_TIME 130
#define UP_TIME 260

Servo smacker;

bool badPosture = false;
bool procrastination = false;
long totalTicksOverThreshold = 0;
long ticksDifference = 0;
long startTime = 0;
const int pressureSensor = A4;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0;        // value read from the pot
int pos = 0;
const int buzzer = 3;


void setup() {

  Serial.begin(9600);
  pinMode(pressureSensor, INPUT_PULLUP); 
  pinMode(buzzer, OUTPUT);
  delay(2000);
  smacker.attach(9);
 
  
}  

void loop() {

    sensorValue = analogRead(pressureSensor);

    if (Serial.available() > 0) {
      // read the incoming byte:
      char incomingByte = Serial.read();
      Serial.println(incomingByte);
  
      //Take appropriate action based on flag
      switch (incomingByte) {
        case 'a':
          procrastination = true;
          
          break;
      }
    }

    ticksDifference = sensorValue - 250;
    if (ticksDifference <= -10) {
      totalTicksOverThreshold++; 
    }

    if(totalTicksOverThreshold > 100) {
          Serial.println("Smack");
          badPosture = true;
          totalTicksOverThreshold = 0;
    }
                  
//    // print the results to the serial monitor:                      
    Serial.println(sensorValue); 

    if (badPosture || procrastination) {
      smackUser();
    }

}

void smackUser() {

  tone(buzzer, 1000); // Send 1KHz sound signal...
  delay(1000);        // ...for 1 sec
  noTone(buzzer);

  for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    smacker.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    smacker.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  } 

  badPosture = false;
  procrastination = false;
   
 }

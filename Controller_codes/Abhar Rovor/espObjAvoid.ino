#include <Servo.h> 

#define TrigPin 22
#define EchoPin 24
#define MAX_DISTANCE 200

#define MOTOR_ENA 34
#define In1 35
#define In2 38
#define MOTOR_ENB 42
#define In3 32
#define In4 33

#define servoPin 15 // Define the pin for the servo

Servo myservo;   

void setup() {
  Serial.begin(9600);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  pinMode(In3, OUTPUT);
  pinMode(In4, OUTPUT);
  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  myservo.attach(servoPin);  
  myservo.write(115); 
  delay(2000);
}

void loop() {
  long duration, distance; 
  digitalWrite(TrigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite(TrigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW); 
  duration = pulseIn(EchoPin, HIGH);
  distance = (duration / 2) / 29.1; 
  Serial.print("CM=");
  Serial.println(distance);
   
  if(distance <= 15) {
    Stop();
    delay(100);
    Backward();
    delay(300);
    Stop();
    delay(200); 
    lookRight();
    delay(200);
    lookLeft();
    delay(200);
    TurnRight();
    delay(850);
    Stop();
    delay(300);
  } else {
    Forward();
  }
}

void lookRight() {
    myservo.write(50); 
    delay(500);
    myservo.write(115); 
}

void lookLeft() {
    myservo.write(170); 
    delay(500); 
    myservo.write(115); 
}

void moveStop() {
  digitalWrite(In1, LOW); 
  digitalWrite(In2,LOW); 
  digitalWrite(In3, LOW); 
  digitalWrite(In4, LOW);
} 
  
void Forward() { 
  digitalWrite(In1,LOW);
  digitalWrite(In2,HIGH);                       
  digitalWrite(In3,LOW);
  digitalWrite(In4,HIGH); 
}

void Backward() {
  digitalWrite(In1,HIGH);
  digitalWrite(In2,LOW);                         
  digitalWrite(In3,HIGH);
  digitalWrite(In4,LOW);
}  

void TurnRight() {
  Serial.println("Turn right..");
  digitalWrite(In1, LOW);
  digitalWrite(In2, HIGH);
  digitalWrite(In3, HIGH);
  digitalWrite(In4, LOW);
} 
 
void TurnLeft() {
 Serial.println("Turn left..");
 myservo.write(180);
 digitalWrite(In1, HIGH);
 digitalWrite(In2, LOW);
 digitalWrite(In3, LOW);
 digitalWrite(In4, HIGH); 
}  

void Stop() {
 digitalWrite(In1, LOW);
 digitalWrite(In2, LOW);
 digitalWrite(In3, LOW);
 digitalWrite(In4, LOW); 
}

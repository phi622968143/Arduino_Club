//extend port
#include <SoftwareSerial.h>


SoftwareSerial BT(2,3);
char s;
const byte LEFT1 = 8;  //IN1
const byte LEFT2 = 9;  //IN2
const byte LEFT_PWM = 10;

const byte RIGHT1 = 7;  //IN3
const byte RIGHT2 = 6;  //IN4
const byte RIGHT_PWM = 5;

void setup(){
  BT.begin(9600);//slave
  Serial.begin(9600);//host
  pinmode(LEFT1,OUTPUT);
  pinmode(LEFT2,OUTPUT);
  pinmode(ENA,OUTPUT);
  pinmode(RIGHT1,OUTPUT);
  pinmode(RIGHT2,OUTPUT);
  pinmode(ENB,OUTPUT);
}
void Forward(){
  digitalWrite(LEFT1, HIGH);
  digitalWrite(LEFT2, LOW);
  analogWrite(LEFT_PWM,200);
  
  //右輪
  digitalWrite(RIGHT1, LOW);
  digitalWrite(RIGHT2, HIGH);
  analogWrite(RIGHT_PWM,200);
}
void Backward(){
  digitalWrite(LEFT2, HIGH);
  digitalWrite(LEFT1, LOW);
  analogWrite(LEFT_PWM,150);
  
  //右輪
  digitalWrite(RIGHT2, LOW);
  digitalWrite(RIGHT1, HIGH);
  analogWrite(RIGHT_PWM,150);
}
void Rightward(){
  digitalWrite(LEFT2, HIGH);
  digitalWrite(LEFT1, LOW);
  analogWrite(LEFT_PWM,150);
  
  //右輪
  digitalWrite(RIGHT2, LOW);
  digitalWrite(RIGHT1, HIGH);
  analogWrite(RIGHT_PWM,100);
}
void Leftward(){
  digitalWrite(LEFT2, HIGH);
  digitalWrite(LEFT1, LOW);
  analogWrite(LEFT_PWM,100);
  
  //右輪
  digitalWrite(RIGHT2, LOW);
  digitalWrite(RIGHT1, HIGH);
  analogWrite(RIGHT_PWM,150);
}
void Stop(){
  analogWrite(LEFT_PWM,0);
  analogWrite(RIGHT_PWM,0);
}
void loop(){
  if(BT.avaliable()){
    s=BT.read();
    delay(10);
    switch(s){
      case 'f':
        Forward();
        break;
      case 'b':
        Backward();
        break;
      case 'r':
        Rightward();
        break;
      case 'l':
        Leftward();
        break;
      default: Stop();
    }
  }
}

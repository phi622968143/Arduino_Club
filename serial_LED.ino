char val;
void setup(){
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
}
void loop(){
  val = Serial.read();
  if(val=='o'){  
    digitalWrite(LED_BUILTIN,HIGH);
    Serial.println("OPEN");
  }else if(val=='c'){
    digitalWrite(LED_BUILTIN,LOW);
    Serial.println("close");
  }
}
const byte startPin=8;
const byte endPin=12;
byte lightPin=startPin;

void setup() {
    for(byte pin=startPin;pin<=endPin;pin++){
        pinMode(pi,OUTPUT);
        digitalWrite(pin,LOW);
    }
}

void loop() {
    digitalWrite(lightPin,HIGH);
    delay(300);
    digitalWrite(lightPin,LOW);
    if (lightPin<endPin)
    {   
        lightPin++;
    }else{
        lightPin=startPin;
    }
    
}

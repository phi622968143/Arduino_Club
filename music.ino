#define E5 659
#define C5 523



void setup() {
  pinMode(8,OUTPUT);
}
void loop(){
  tone(8,E5,150);//pin 腳,音高,持續時間
  delay(300);
  tone(8,C5,150);
}

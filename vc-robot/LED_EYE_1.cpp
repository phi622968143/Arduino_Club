#include <LedControl.h> 

int DIN = 12;
int CS =  11;
int CLK = 10;



byte smile[8]=   {0x3C,0x42,0xA5,0x81,0xA5,0x99,0x42,0x3C};  //微笑
byte love_1[8]=   {0x00,0x66,0x99,0x81,0x42,0x24,0x18,0x00}; //愛心-1
byte love_2[8]=   {0x00,0x66,0xff,0xff,0x7e,0x3c,0x18,0x00}; //愛心-2
byte abc[8]= {0x10,0x28,0x28,0x44,0x44,0x82,0x82,0x00 };//>
byte abc2[8]= {0x10,0x28,0x28,0x28,0x44,0x44,0x44,0x00 };//>-2
byte glasses[8]={0x70,0x48,0x44,0x44,0x44,0x44,0x48,0x70};
byte circle[8]= {0x3c,0x42,0x99,0xA5,0XA5,0X99,0X42,0X3C};
byte xx[8]={0xC3,0XE7,0X7E,0X3C,0X3C,0X7E,0XE7,0XC3};


LedControl lc=LedControl(DIN,CLK,CS,0);

void setup(){
 lc.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 //lc.setIntensity(0,7);      // Set the brightness to maximum value
 lc.clearDisplay(0);         // and clear the display
}

void loop(){ 

   // printByte(smile);
    lc.setIntensity(0,14);
    delay(1000);
    
    //printByte(love_1); 
    lc.setIntensity(0,9);    
    delay(1000);

    //printByte(love_2);
    lc.setIntensity(0,7);     
    delay(1000);
    //printByte(glasses);
    lc.setIntensity(0,12); 
    delay(1000);

    printByte(abc); 
    lc.setIntensity(0,7);    
    delay(1000);
    
    printByte(abc2); 
    lc.setIntensity(0,7);    
    delay(1000);

    //printByte(circle);
    lc.setIntensity(0,5); 
    delay(1000);
    //printByte(xx);
    lc.setIntensity(0,8); 
    delay(1000);


    
    
    //printLetter();
    
   
    lc.clearDisplay(0);
    
    delay(1000);
}



void printByte(byte character [])
{
  int i = 0;
  for(i=0;i<8;i++)
  {
    lc.setRow(0,i,character[i]);
  }
}

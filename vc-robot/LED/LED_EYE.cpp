#include <LedControl.h>

int DIN1 = 12;  // Data In for Matrix 1
int CS1 =  11;  // Chip Select for Matrix 1
int CLK1 = 10;  // Clock for Matrix 1

int DIN2 = 9;   // Data In for Matrix 2
int CS2 =  8;   // Chip Select for Matrix 2
int CLK2 = 7;   // Clock for Matrix 2

// 定义字节图案
byte smile[8] = {0x3C, 0x42, 0xA5, 0x81, 0xA5, 0x99, 0x42, 0x3C};  // 微笑
byte love_1[8] = {0x00, 0x66, 0x99, 0x81, 0x42, 0x24, 0x18, 0x00}; // 爱心-1
byte love_2[8] = {0x00, 0x66, 0xFF, 0xFF, 0x7E, 0x3C, 0x18, 0x00}; // 爱心-2
byte abc[8] = {0x10, 0x28, 0x28, 0x44, 0x44, 0x82, 0x82, 0x00};    // >
byte abc2[8] = {0x10, 0x28, 0x28, 0x28, 0x44, 0x44, 0x44, 0x00};   // >-2
byte glasses[8] = {0x70, 0x48, 0x44, 0x44, 0x44, 0x44, 0x48, 0x70}; // 眼镜
byte circle[8] = {0x3C, 0x42, 0x99, 0xA5, 0xA5, 0x99, 0x42, 0x3C};  // 圆形
byte xx[8] = {0xC3, 0xE7, 0x7E, 0x3C, 0x3C, 0x7E, 0xE7, 0xC3};      // XX

LedControl lc1 = LedControl(DIN1, CLK1, CS1, 1); // 初始化 LED 控制器 1
LedControl lc2 = LedControl(DIN2, CLK2, CS2, 1); // 初始化 LED 控制器 2

void setup() {
  lc1.shutdown(0, false);  // 启动 MAX72XX for Matrix 1
  lc1.setIntensity(0, 7);  // 设置亮度 for Matrix 1
  lc1.clearDisplay(0);     // 清空显示屏 for Matrix 1

  lc2.shutdown(0, false);  // 启动 MAX72XX for Matrix 2
  lc2.setIntensity(0, 7);  // 设置亮度 for Matrix 2
  lc2.clearDisplay(0);     // 清空显示屏 for Matrix 2
}

void loop() {
  displayPattern(lc1, smile, 14);
  displayPattern(lc2, smile, 14);
  delay(1000);
  displayPattern(lc1, love_2, 12);
  displayPattern(lc2, love_1, 12);
  delay(1000);
  displayPattern(lc1, abc, 7);
  displayPattern(lc2, abc2, 7);
  delay(1000);
  displayPattern(lc1, xx, 2);
  displayPattern(lc2, xx, 2);
  delay(1000);
  displayPattern(lc1, circle, 2);
  displayPattern(lc2, circle, 2);

  lc1.clearDisplay(0);  
  lc2.clearDisplay(0);  
  delay(1000);
}

void displayPattern(LedControl &lc, byte character[], int intensity) {
  lc.setIntensity(0, intensity);
  printByte(lc, character);
  delay(1000);
}

void printByte(LedControl &lc, byte character[]) {
  for (int i = 0; i < 8; i++) {
    lc.setRow(0, i, character[i]);
  }
}

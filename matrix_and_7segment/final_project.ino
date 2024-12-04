#include "LedController.hpp"

// --------------------- MAX7219 點陣 LED 模組 ---------------------
// 定義 CS 腳位
#define CS 2
// 建立 LedController<幾列LED模組,幾行LED模組> LED矩陣名稱
LedController<1, 1> lc;

// 圖片數據，使用二維陣列表示 8x8 圖片
ByteBlock IMAGES[] = {
{
  0b01111000,
  0b00110000,
  0b00011110,
  0b00111001,
  0b01001101,
  0b00010100,
  0b00100010,
  0b01000001
},{
  0b01111000,
  0b00110000,
  0b00011100,
  0b00111010,
  0b01001101,
  0b00010100,
  0b00100110,
  0b01100010
},{
  0b01111000,
  0b00110000,
  0b00011100,
  0b00111010,
  0b00001100,
  0b00010100,
  0b00100100,
  0b01100010
},{
  0b01111000,
  0b00110000,
  0b00011100,
  0b00011000,
  0b00101100,
  0b00010100,
  0b00010100,
  0b00100100
},{
  0b01111000,
  0b00110000,
  0b00011100,
  0b00011100,
  0b00111100,
  0b00001100,
  0b00010100,
  0b00100100
},{
  0b01111000,
  0b00110000,
  0b00011000,
  0b00011000,
  0b00011100,
  0b00001100,
  0b00010100,
  0b00010100
},{
  0b01111000,
  0b00110000,
  0b00111000,
  0b00001100,
  0b00111000,
  0b00011000,
  0b00010100,
  0b00100100
},{
  0b01111000,
  0b00110000,
  0b00111100,
  0b00011000,
  0b00111000,
  0b00010100,
  0b00010100,
  0b00100100
},{
  0b01111000,
  0b00110000,
  0b00111100,
  0b00111010,
  0b00011000,
  0b00010100,
  0b00100100,
  0b00100010
},{
  0b01111000,
  0b00110000,
  0b00111100,
  0b00111010,
  0b01011001,
  0b00010100,
  0b00100110,
  0b01100010
},{
  0b01111000,
  0b00110000,
  0b00111110,
  0b00101001,
  0b01011001,
  0b00010100,
  0b00100010,
  0b01000001
}};
const int IMAGES_LEN = sizeof(IMAGES) / sizeof(IMAGES[0]);

// -------------------- 七段顯示器部分 --------------------
int pins[] = {15, 4, 14, 12, 13, 5, 16}; // 對應 A, B, C, D, E, F, G

// 七段顯示的數字對應
int numSegments[10][7] = {
  {0, 0, 0, 0, 0, 0, 1}, // 0
  {1, 0, 0, 1, 1, 1, 1}, // 1
  {0, 0, 1, 0, 0, 1, 0}, // 2
  {0, 0, 0, 0, 1, 1, 0}, // 3
  {1, 0, 0, 1, 1, 0, 0}, // 4
  {0, 1, 0, 0, 1, 0, 0}, // 5
  {0, 1, 0, 0, 0, 0, 0}, // 6
  {0, 0, 0, 1, 1, 1, 1}, // 7
  {0, 0, 0, 0, 0, 0, 0}, // 8
  {0, 0, 0, 0, 1, 0, 0}  // 9
};

void seg_display(int num) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(pins[i], numSegments[num][i]);
  }
}

// -------------------- 時間追蹤變數 --------------------
int previousImageMillis = 0; // MAX7219 上次更新時間
int previousSevenSegmentMillis = 0; // 七段顯示器上次更新時間

int imageInterval = 50; // MAX7219 更新間隔 (ms)
int sevenSegmentInterval = 1000; // 七段顯示器更新間隔 (ms)

int currentImageIndex = 0; // 當前顯示的圖片索引
int currentNumber = 5; // 七段顯示器當前顯示的數字

void setup() {
  // 初始化 LedController
  lc = LedController<1, 1>(CS);
  lc.clearMatrix(); // 清空 MAX7219 矩陣
  
  // 初始化七段顯示器腳位
  for (int i = 0; i < 7; i++) {
    pinMode(pins[i], OUTPUT);
  }
}

void loop() {
  int currentMillis = millis();

  // 更新 MAX7219 動畫
  if (currentMillis - previousImageMillis >= imageInterval) {
    previousImageMillis = currentMillis;
    lc.displayOnSegment(0, IMAGES[currentImageIndex]);
    currentImageIndex = (currentImageIndex + 1) % IMAGES_LEN; // 循環播放圖片
  }

  // 更新七段顯示器倒數
  if (currentMillis - previousSevenSegmentMillis >= sevenSegmentInterval) {
    previousSevenSegmentMillis = currentMillis;
    seg_display(currentNumber);
    currentNumber--;
    if (currentNumber < 0) {
      currentNumber = 5; // 重置倒數
    }
  }
}

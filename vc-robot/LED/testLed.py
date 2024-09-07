from machine import Pin, SPI
from LEDMatrix import Matrix8x8
import time

spi1 = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
cs1 = Pin(9, Pin.OUT)
display1 = Matrix8x8(spi1, cs1, 1)

spi2 = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(6), mosi=Pin(7))
cs2 = Pin(13, Pin.OUT)
display2 = Matrix8x8(spi2, cs2, 1)


display1.brightness(8)
display2.brightness(13)

smile = [0x3C, 0x42, 0xA5, 0x81, 0xA5, 0x99, 0x42, 0x3C]  # smile
love_1 = [0x00, 0x66, 0x99, 0x81, 0x42, 0x24, 0x18, 0x00] # heart1
love_2 = [0x00, 0x66, 0xFF, 0xFF, 0x7E, 0x3C, 0x18, 0x00] # heart2
abc = [0x10, 0x28, 0x28, 0x44, 0x44, 0x82, 0x82, 0x00]
abc2 = [0x10, 0x28, 0x28, 0x28, 0x44, 0x44, 0x44, 0x00]
glasses = [0x70, 0x48, 0x44, 0x44, 0x44, 0x44, 0x48, 0x70]
circle = [0x3C, 0x42, 0x99, 0xA5, 0xA5, 0x99, 0x42, 0x3C]
xx = [0xC3, 0xE7, 0x7E, 0x3C, 0x3C, 0x7E, 0xE7, 0xC3]
def display_pattern(display, pattern):
        display.fill(0)
        for y in range(8):
            display.buffer[y] = pattern[y]
        display.show()
def test_patterns():
    patterns = [smile, love_2, abc, xx, circle]
    for pattern in patterns:
        display1.brightness(8)
        display2.brightness(8)
        display_pattern(display1, pattern)
        display_pattern(display2, pattern)
        time.sleep(0.7)

while True:
    test_patterns()
    time.sleep(0.5)

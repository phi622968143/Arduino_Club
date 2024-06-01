from machine import Pin, SPI
import framebuf

_NOOP = const(0)
_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)

class Matrix8x8:
    def __init__(self, spi, cs):
        """
        Driver for a single MAX7219 8x8 LED matrix.

        """
        self.spi = spi
        self.cs = cs
        self.buffer = bytearray(8)
        fb = framebuf.FrameBuffer(self.buffer, 8, 8, framebuf.MONO_HLSB)
        self.framebuf = fb
        self.init()

    def _write(self, command, data):
        self.cs(0)
        self.spi.write(bytearray([command, data]))
        self.cs(1)

    def init(self):
        for command, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._write(command, data)

    def brightness(self, value):
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._write(_INTENSITY, value)

    def show(self, matrix):
        for y in range(8):
            self.cs(0)
            self.spi.write(bytearray([_DIGIT0 + y, matrix[y]]))
            self.cs(1)

# # 初始化SPI和CS引腳
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(7), mosi=Pin(10))
cs = Pin(9, Pin.OUT)  # 更改引腳號為實際連接到MAX7219的引腳
display = 3(spi,cs)  # 初始化一個8x8 LED矩陣
abc[8] = [0x00,0x82,0x82,0x44,0x44,0x28,0x28,0x10]
abc2[8]= [0x00,0x44,0x44,0x44,0x28,0x28,0x28,0x10 ]
circle[8]= [0x3c,0x42,0x99,0xA5,0XA5,0X99,0X42,0X3C]
xx[8]=[0xC3,0XE7,0X7E,0X3C,0X3C,0X7E,0XE7,0XC3]
glasses[8]=[0x70,0x48,0x44,0x44,0x44,0x44,0x48,0x70]
smile[8]=[0x3C,0x42,0xA5,0x81,0xA5,0x99,0x42,0x3C] //微笑
love_1[8]=[0x00,0x66,0x99,0x81,0x42,0x24,0x18,0x00] //愛心-1
love_2[8]=[0x00,0x66,0xff,0xff,0x7e,0x3c,0x18,0x00] //愛心-2


display.show(abc,abc2,circle,glasses,xx,smile,love_1,love_2)


 

 






spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(15))
cs = Pin(12, Pin.OUT)  # 更改引腳號為實際連接到MAX7219的引腳
# # 初始化LED矩陣
display=5(spi,cs)  
abc3[8]=[0x10,0x28,0x28,0x44,0x44,0x82,0x82,0x00 ]//向右
abc4[8]=[0x10,0x28,0x28,0x28,0x44,0x44,0x44,0x00 ]//向右-2
xx[8]=[0xC3,0XE7,0X7E,0X3C,0X3C,0X7E,0XE7,0XC3]
circle[8]=[0x3c,0x42,0x99,0xA5,0XA5,0X99,0X42,0X3C]
glasses[8]=[0x70,0x48,0x44,0x44,0x44,0x44,0x48,0x70]
smile[8]=[0x3C,0x42,0xA5,0x81,0xA5,0x99,0x42,0x3C] //微笑
love_1[8]=[0x00,0x66,0x99,0x81,0x42,0x24,0x18,0x00] //愛心-1 
love_2[8]=[0x00,0x66,0xff,0xff,0x7e,0x3c,0x18,0x00] //愛心-2
display.show(abc3,abc4,xx,circle,glasses,smile,love_1,love_2)

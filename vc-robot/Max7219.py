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
# spi = SPI(1, baudrate=10000000, polarity=0, phase=0)  # 需要檢查這些參數是否與Pico的硬體兼容
# cs = Pin(5, Pin.OUT)  # 更改引腳號為實際連接到MAX7219的引腳

# # 初始化LED矩陣
# display = Matrix8x8(spi, cs)  # 初始化一個8x8 LED矩陣

# # 定義要顯示的矩陣
# custom_matrix = [
#     0b11111111,
#     0b00000000,
#     0b00000000,
#     0b11111111,
#     0b00000000,
#     0b00000000,
#     0b11111111,
#     0b00000000,
# ]

# # 顯示矩陣
# display.show(custom_matrix)

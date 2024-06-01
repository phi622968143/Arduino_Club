from machine import SPI, Pin

class LEDMatrix:
    def __init__(self, cs_pin, sck_pin, mosi_pin, num_cols=8, num_rows=8, baudrate=100000):
        self.spi = SPI(1, baudrate=baudrate, sck=Pin(sck_pin), mosi=Pin(mosi_pin))
        self.cs_pin = Pin(cs_pin, Pin.OUT)
        self.cs_pin.value(1)  # Chip select high initially
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.init_matrix()

    def init_matrix(self):
        # Initialize MAX7219 registers
        self.cs_pin.value(0)  # Chip select low
        self.spi.write(bytes([0x09, 0x00]))  # Decode mode: no decode
        self.spi.write(bytes([0x0A, 0x06]))  # Intensity: medium intensity
        self.spi.write(bytes([0x0B, 0x07]))  # Scan limit: all rows
        self.spi.write(bytes([0x0C, 0x01]))  # Shutdown: normal operation
        self.spi.write(bytes([0x0F, 0x00]))  # Display test: off
        self.cs_pin.value(1)  # Chip select high

    def set_led(self, row, col, state):
        # Set LED at specified row and column to given state (0 or 1)
        if row < 0 or row >= self.num_rows or col < 0 or col >= self.num_cols:
            return
        self.cs_pin.value(0)  # Chip select low
        address = col + 1  # Address for MAX7219
        data = 1 << row if state else 0
        self.spi.write(bytes([address, data]))
        self.cs_pin.value(1)  # Chip select high

    def clear(self):
        # Clear all LEDs
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.set_led(row, col, 0)

    def display_pattern(self, pattern):
        # Display a predefined or custom pattern
        if len(pattern) != self.num_cols * self.num_rows:
            return
        self.clear()
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                index = col * self.num_cols + row
                self.set_led(row, col, pattern[index])

# Example usage of LEDMatrix library
from LEDMatrix import LEDMatrix
import time
# Initialize LED matrix
led_matrix = LEDMatrix(cs_pin=5, sck_pin=10, mosi_pin=11)

# Define a custom pattern
custom_pattern = [
    1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1,
    1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1,
    1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1,
    1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1
]

# Display the custom pattern
for i in range (10):
    led_matrix.display_pattern(custom_pattern)
    time.sleep(100)

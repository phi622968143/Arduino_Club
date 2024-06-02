from machine import UART, Pin
from time import sleep_ms
from DFPlayer import DFPlayer  # Assume DFPlayer class exists in DFPlayer.py file

# Define UART connection
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Define control pins for DFPlayer
busy_pin = Pin(2, Pin.IN, Pin.PULL_UP)  # Assume DFPlayer's BUSY pin is connected to GPIO 2
tx_pin = 4  # Assume UART's TX pin is connected to GPIO 4
rx_pin = 5  # Assume UART's RX pin is connected to GPIO 5

# Initialize DFPlayer object
player = DFPlayer(uart, tx_pin, rx_pin, busy_pin)

# Play MP3
player.playMP3(1)  # Play the first MP3 file

# Wait for playback to finish
while player.queryBusy():
    sleep_ms(100)

# Pause playback
player.pause()

# Wait for a while
sleep_ms(2000)

# Resume playback
player.resume()

# Adjust volume
player.setVolume(20)  # Set volume to 20

# Wait for a while
sleep_ms(5000)

# Stop playback
player.pause()
from machine import UART, Pin
from time import sleep_ms
from DFPlayer import DFPlayer  # Assume DFPlayer class exists in DFPlayer.py file

# Define UART connection
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Define control pins for DFPlayer
busy_pin = Pin(2, Pin.IN, Pin.PULL_UP)  # Assume DFPlayer's BUSY pin is connected to GPIO 2
tx_pin = 4  # Assume UART's TX pin is connected to GPIO 4
rx_pin = 5  # Assume UART's RX pin is connected to GPIO 5

# Initialize DFPlayer object
player = DFPlayer(uart, tx_pin, rx_pin, busy_pin)

# Play MP3
player.playMP3(1)  # Play the first MP3 file

# Wait for playback to finish
while player.queryBusy():
    sleep_ms(100)

# Pause playback
player.pause()

# Wait for a while
sleep_ms(2000)

# Resume playback
player.resume()

# Adjust volume
player.setVolume(20)  # Set volume to 20

# Wait for a while
sleep_ms(5000)

# Stop playback
player.pause()


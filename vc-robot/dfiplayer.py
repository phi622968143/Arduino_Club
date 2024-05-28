import machine
import time

# Constants for communication
START_BYTE = 0x7E
VERSION = 0xFF
COMMAND_LENGTH = 0x06
FEEDBACK = 0x00
END_BYTE = 0xEF

# Commands for MP3 module
SET_VOLUME = 0x06
PLAY_FOLDER_TRACK = 0x0F

# Function to send command to MP3 module
def send_command(command, param1=0x00, param2=0x00):
    checksum = 0xFFFF - (VERSION + COMMAND_LENGTH + command + FEEDBACK + param1 + param2) + 1
    high_byte = (checksum >> 8) & 0xFF
    low_byte = checksum & 0xFF
    command_list = [START_BYTE, VERSION, COMMAND_LENGTH, command, FEEDBACK, param1, param2, high_byte, low_byte, END_BYTE]
    
    uart.write(bytes(command_list))

# Initialize UART
uart = machine.UART(1, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5))

# Notification class equivalent
class Mp3Notify:
    @staticmethod
    def println_source_action(source, action):
        sources = []
        if source & 0x01:  # Assuming 0x01 represents SD Card
            sources.append("SD Card")
        if source & 0x02:  # Assuming 0x02 represents USB Disk
            sources.append("USB Disk")
        if source & 0x04:  # Assuming 0x04 represents Flash
            sources.append("Flash")
        print(", ".join(sources) + f", {action}")

    @staticmethod
    def on_error(error_code):
        print(f"\nCom Error {error_code}")

    @staticmethod
    def on_play_finished(track):
        print(f"Play finished for #{track}")

    @staticmethod
    def on_play_source_online(source):
        Mp3Notify.println_source_action(source, "online")

    @staticmethod
    def on_play_source_inserted(source):
        Mp3Notify.println_source_action(source, "inserted")

    @staticmethod
    def on_play_source_removed(source):
        Mp3Notify.println_source_action(source, "removed")

# Setup function
def setup():
    print("Initializing MP3 Player")
    send_command(SET_VOLUME, 0x1E)  # Set volume to 30

# Loop function
def loop():
    for i in range(7, 0, -1):
        send_command(PLAY_FOLDER_TRACK, 0x01, i)
        time.sleep(1)

# Main execution
setup()

while True:
    loop()
    time.sleep(10)  # Adding delay to prevent rapid loop execution

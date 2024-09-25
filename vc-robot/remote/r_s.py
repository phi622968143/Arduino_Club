import socket
import network
import time
from action import servo_default_action, forward_action
from DFplayer import DFPlayer
from testLed import *

# WiFi configuration
def read_wifi_config(filename):
    wifi_config = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        wifi_config['WIFI_SSID'] = lines[0].strip()
        wifi_config['WIFI_PASSWORD'] = lines[1].strip()
    return wifi_config

wifi_config = read_wifi_config('wifi.conf')
WIFI_SSID = wifi_config['WIFI_SSID']
WIFI_PASSWORD = wifi_config['WIFI_PASSWORD']

# Connect to WiFi
print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    pass

print("WiFi connected:", wifi.ifconfig()[0])
test_patterns()

# Define actions for each byte value
def action_0(byte):
    forward_action()

def action_1(byte):
    player = DFPlayer(uart_port=1, baud_rate=9600, rx_pin=5, tx_pin=4)
    player.set_volume(12)
    player.play_track(1)

def action_2(byte):
    for i in range(20):  
        love_patterns()
        time.sleep(0.7)

def default_action(byte):
    print("Default action for byte:", byte)

def timeout_action():
    print("Timeout occurred, performing default action.")
    servo_default_action()

# Mapping byte values to corresponding actions
action_map = {
    0: action_0,
    1: action_1,
    2: action_2,
}

# Configure the server
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 2000       # Arbitrary port number

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Waiting for a connection...')


try:
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print('Connected to:', client_address)

        try:
            while True:
                # Receive binary data
                data = client_socket.recv(1024)
                if not data:
                    break  # No more data, break the loop
                
                for byte in data:
                    # Perform action based on byte value
                    action = action_map.get(byte, default_action)
                    action(byte)
                    
                    # Send acknowledgment back to the sender
                    ack = bytes([byte])  # ACK with the received byte
                    client_socket.sendall(ack)
        
        finally:
            # Close the client connection
            print('Closing connection with:', client_address)
            client_socket.close()

finally:
    # Close the server socket
    print('Closing server socket...')
    server_socket.close()

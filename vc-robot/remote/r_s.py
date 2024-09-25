import socket
import network
import time
from testLed import led_patterns
from mp3play import play
from action import Action

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
    print("Waiting for WiFi connection...")
    time.sleep(1)

print("WiFi connected:", wifi.ifconfig()[0])

# Define actions for each byte value

def action_0(byte):
    
    action=Action()
    action.servo_default_action()
def action_1(byte):
    print("Playing music")
    play.music()

def action_2(byte):
    matrix=led_patterns()
    time.sleep(5)
    for i in range(20):
        matrix.love_patterns()

def default_action(byte):
    print("Default action for byte:", byte)

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
                time.sleep(2)
                data = client_socket.recv(1024)
                if not data:
                    print("No data received, closing connection.")
                    break
                
                # Print received data
                print("Received data:", data)

                for byte in data:
                    print(f"Processing byte: {byte}")
                    
                    # Perform action based on byte value
                    if byte == 0:
                        action_0(byte)
                    elif byte == 10:
                        action_1(byte)
                    elif byte == 2:
                        action_2(byte)
                    else:
                        default_action(byte)
                    
                    # Send acknowledgment back to the sender
                    ack = bytes([byte])  # ACK with the received byte
                    client_socket.sendall(ack)
        
        except Exception as e:
            print(f"Error during communication: {e}")

        finally:
            # Close the client connection
            print('Closing connection with:', client_address)
            client_socket.close()

finally:
    # Close the server socket
    print('Closing server socket...')
    server_socket.close()

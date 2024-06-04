from machine import UART
import time

class DFPlayer:
    def __init__(self, uart_port, baud_rate, rx_pin, tx_pin):
        self.uart = UART(uart_port, baud_rate, rx=rx_pin, tx=tx_pin)
        self.uart.init(baud_rate, bits=8, parity=None, stop=1)
        time.sleep(1)  # 等待初始化完成

    def send_command(self, command, param):
        data = bytearray([0x7E, 0xFF, 0x06, command, 0x00, (param >> 8) & 0xFF, param & 0xFF, 0xEF])
        self.uart.write(data)

    def play_track(self, track_num):
        self.send_command(0x03, track_num)

    def set_volume(self, volume):
        self.send_command(0x06, volume)

    def pause(self):
        self.send_command(0x0E, 0)

    def resume(self):
        self.send_command(0x0D, 0)
    def next_track(self):
        self.send_command(0x01, 0)

    def previous_track(self):
        self.send_command(0x02, 0)

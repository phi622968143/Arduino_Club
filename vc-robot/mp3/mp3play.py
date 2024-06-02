from machine import UART, Pin
from DFPlayer import DFPlayer 
from time import sleep


player = DFPlayer(uart_port=1, baud_rate=9600, rx_pin=5, tx_pin=4)


player.set_volume(12)


player.play_track(1)

sleep(10)

player.pause()


sleep(2)
player.next_track()

sleep(10)


player.previous_track()
player.previous_track()


sleep(10)


player.resume()


sleep(5)


player.pause()

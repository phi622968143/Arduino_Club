import time
import asyncio
from servo import Servo

rt = Servo(0)
rb = Servo(1)
lt = Servo(6)
lb = Servo(7)

def action_test():
	lt.lerp(0, 180, 5 , 0.01)
def servo_default_action():
	print("Conducting.....")
	for i in range(10):
    		lt.lerp(-15, 0, 1, 0.01)
    		lt.lerp(0, -15, 1, 0.01)
		time.sleep(0.1)
		rt.lerp(0, 30, 2, 0.1)
		rt.lerp(30, 0, 2, 0.1)
	for i in range(10):
    		rt.lerp(30, 0, 2, 0.1)
    		rt.lerp(0, 30, 2, 0.1)
		time.sleep(0.1)
		lt.lerp(0, -15, 1, 0.01)
		lt.lerp(-15, 0, 1, 0.01)
def forward_action():
	for i in range(10):
		lb.lerp(60, 120, 1, 0.01)
		lb.lerp(120, 60, 1, 0.01)
	time.sleep(0.1)
	for i in range(10):
		rb.lerp(0, 90, 1, 0.01)
		rb.lerp(90, 0, 1, 0.01)

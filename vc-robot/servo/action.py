import time
import asyncio
from servo import Servo

rt = Servo(0)
rb = Servo(1)
lt = Servo(2)
lb = Servo(3)

def action_test():
    rt.lerp(-19, 180, 1 , 0.01)

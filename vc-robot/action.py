import time
import asyncio
from servo import Servo

rt = Servo(0)
rb = Servo(1)
lt = Servo(2)
lb = Servo(3)

async def action_test():
    motors = [rt, rb, lt, lb]
    angle_steps = [(int(rt.read()), 180, 1), (int(rb.read()), 30, 1), (int(lt.read()),0,-1),(int(lb.read()),120,-1)]  # Example angle steps for each motor
    await Servo.valerp(motors, angle_steps, 0.01)

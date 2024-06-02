import machine
import math
import time
import asyncio

class Servo:
    def __init__(self, pin_id, min_us=544.0, max_us=2400.0, min_deg=0.0, max_deg=180.0, freq=50, debug=True):
        self.pwm = machine.PWM(machine.Pin(pin_id))
        self.pwm.freq(freq)
        self.current_us = 0.0
        self._slope = (min_us - max_us) / (math.radians(min_deg) - math.radians(max_deg))
        self._offset = min_us
        self.debug = True

    def write(self, deg):
        self.write_rad(math.radians(deg))

    def read(self):
        return math.degrees(self.read_rad())

    def write_rad(self, rad):
        self.write_us(rad * self._slope + self._offset)

    def read_rad(self):
        return (self.current_us - self._offset) / self._slope

    def write_us(self, us):
        self.current_us = us
        self.pwm.duty_ns(int(self.current_us * 1000.0))

    def read_us(self):
        return self.current_us

    def off(self):
        self.pwm.duty_ns(0)

    def log(self, message):
        if self.debug:
            print(message)

    def lerp(self,start,stop,step,delay):
        for angle in range(start, stop, step):
            self.write(angle)
            time.sleep(delay)
            self.log(angle)

    async def alerp(self, start, stop, step, delay):
        for angle in range(start, stop, step):
            self.write(angle)
            await asyncio.sleep(delay)
            self.log(angle)
            
    @staticmethod
    def vlerp(motors, angle_steps, delay):
        tasks = []
        for motor, steps in zip(motors, angle_steps):
            tasks.append(motor.lerp(*steps, delay))
        for task in tasks:
            task.result()  # Wait for each task to complete


    @staticmethod
    async def valerp(motors, angle_steps, delay):
        tasks = []
        for motor, steps in zip(motors, angle_steps):
            tasks.append(motor.alerp(*steps, delay))
        await asyncio.gather(*tasks)

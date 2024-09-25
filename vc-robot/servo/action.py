import time
from servo import Servo

class Action:
    def __init__(self):
        # Initialize servos
        self.rt = Servo(2)
        self.rb = Servo(3)
        self.lt = Servo(0)
        self.lb = Servo(1)

    def action_test(self):
        self.lt.lerp(0, 180, 5, 0.01)

    def servo_default_action(self):
        print("Conducting.....")
        for _ in range(10):
            self.lt.lerp(-15, 0, 1, 0.01)
            self.lt.lerp(0, -15, 1, 0.01)
            time.sleep(0.1)
            self.rt.lerp(0, 30, 2, 0.1)
            self.rt.lerp(30, 0, 2, 0.1)
        
        for _ in range(10):
            self.rt.lerp(30, 0, 2, 0.1)
            self.rt.lerp(0, 30, 2, 0.1)
            time.sleep(0.1)
            self.lt.lerp(0, -15, 1, 0.01)
            self.lt.lerp(-15, 0, 1, 0.01)

    def forward_action(self):
       
        for _ in range(10):
            self.lb.lerp(60, 120, 1, 0.01)
            self.lb.lerp(120, 60, 1, 0.01)
        time.sleep(0.1)

        for _ in range(10):
            self.rb.lerp(0, 90, 1, 0.01)
            self.rb.lerp(90, 0, 1, 0.01)

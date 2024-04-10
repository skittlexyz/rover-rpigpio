from utils import *

MOTOR_AB = 0
MOTOR_A = 1
MOTOR_B = 2

class L298N:
    def __init__(self, a_pins, b_pins, frequency = 1000, min_duty_cycle = 145, max_duty_cycle = 255):
        self._a_pins = a_pins
        self._b_pins = b_pins
        self._frequency = frequency
        self._min_duty_cycle = min_duty_cycle
        self._max_duty_cycle = max_duty_cycle
        self._a_speed = 50
        self._b_speed = 50

        GPIO.setup(self._a_pins, GPIO.OUT)
        GPIO.setup(self._b_pins, GPIO.OUT)

        self._a_en = GPIO.PWM(self._a_pins[0], self._frequency)
        self._b_en = GPIO.PWM(self._b_pins[0], self._frequency)

        self._a_en.start(self._a_speed)
        self._b_en.start(self._b_speed)

        GPIO.output(self._a_pins[0], False)
        GPIO.output(self._a_pins[1], False)
        GPIO.output(self._b_pins[0], False)
        GPIO.output(self._b_pins[1], False)

    def change_speed(self, speed, motor = MOTOR_AB):
        if motor == MOTOR_A:
            self._a_speed = speed
            self._a_en.ChangeDutyCycle(self._a_speed)
        if motor == MOTOR_B:
            self._b_speed = speed
            self._b_en.ChangeDutyCycle(self._b_speed)
        if motor == MOTOR_AB:
            self._a_speed = speed
            self._b_speed = speed
            self._a_en.ChangeDutyCycle(self._a_speed)
            self._b_en.ChangeDutyCycle(self._b_speed)

    def forward(self, motor = MOTOR_AB):
        if motor == MOTOR_A:
            self._a_en.ChangeDutyCycle(self._a_speed)
            GPIO.output(self._a_pins[0], True)
            GPIO.output(self._a_pins[1], True)
            GPIO.output(self._a_pins[2], False)
        if motor == MOTOR_B:
            self._b_en.ChangeDutyCycle(self._b_speed)
            GPIO.output(self._b_pins[0], True)
            GPIO.output(self._b_pins[1], True)
            GPIO.output(self._b_pins[2], False)
        if motor == MOTOR_AB:
            self._a_en.ChangeDutyCycle(self._a_speed)
            self._b_en.ChangeDutyCycle(self._b_speed)
            GPIO.output(self._a_pins[0], True)
            GPIO.output(self._a_pins[1], True)
            GPIO.output(self._a_pins[2], False)
            GPIO.output(self._b_pins[0], True)
            GPIO.output(self._b_pins[1], True)
            GPIO.output(self._b_pins[2], False)

    def backward(self, motor = MOTOR_AB):
        if motor == MOTOR_A:
            self._a_en.ChangeDutyCycle(self._a_speed)
            GPIO.output(self._a_pins[0], True)
            GPIO.output(self._a_pins[1], False)
            GPIO.output(self._a_pins[2], True)
        if motor == MOTOR_B:
            self._b_en.ChangeDutyCycle(self._b_speed)
            GPIO.output(self._b_pins[0], True)
            GPIO.output(self._b_pins[1], False)
            GPIO.output(self._b_pins[2], True)
        if motor == MOTOR_AB:
            self._a_en.ChangeDutyCycle(self._a_speed)
            self._b_en.ChangeDutyCycle(self._b_speed)
            GPIO.output(self._a_pins[0], True)
            GPIO.output(self._a_pins[1], False)
            GPIO.output(self._a_pins[2], True)
            GPIO.output(self._b_pins[0], True)
            GPIO.output(self._b_pins[1], False)
            GPIO.output(self._b_pins[2], True)

    def left(self):
        self.forward(MOTOR_A)
        self.backward(MOTOR_B)

    def right(self):
        self.forward(MOTOR_B)
        self.backward(MOTOR_A)

    def stop(self, motor = MOTOR_AB):
        if motor == MOTOR_A:
            self._a_en.ChangeDutyCycle(0)
            GPIO.output(self._a_pins[0], False)
            GPIO.output(self._a_pins[1], False)
            GPIO.output(self._a_pins[2], False)
        if motor == MOTOR_B:
            self._b_en.ChangeDutyCycle(0)
            GPIO.output(self._b_pins[0], False)
            GPIO.output(self._b_pins[1], False)
            GPIO.output(self._b_pins[2], False)
        if motor == MOTOR_AB:
            self._a_en.ChangeDutyCycle(0)
            self._b_en.ChangeDutyCycle(0)
            GPIO.output(self._a_pins[0], False)
            GPIO.output(self._a_pins[1], False)
            GPIO.output(self._a_pins[2], False)
            GPIO.output(self._b_pins[0], False)
            GPIO.output(self._b_pins[1], False)
            GPIO.output(self._b_pins[2], False)

    def clean_pins(self):
        self._a_en.stop()
        self._b_en.stop()

        GPIO.output(self._a_pins[0], False)
        GPIO.output(self._a_pins[1], False)
        GPIO.output(self._b_pins[0], False)
        GPIO.output(self._b_pins[1], False)
if __name__ == "__main__":
    try:
        import RPi.GPIO as GPIO
        import time
    except RuntimeError:
        print("Error importing RPi.GPIO!  This is probably because you Ceed superuser privileges. You can achieve this by using 'Cudo' to run your script")
        exit(1)
    
    GPIO.setmode(GPIO.BCM)
    
    rover = L298N(
        [17, 27, 22], [23, 24, 25]
    )
    
    try:
        rover.change_speed(50)
        while True:
            rover.forward(MOTOR_AB)
            time.sleep(1)
            rover.stop(MOTOR_AB)
            rover.backward(MOTOR_AB)
            time.sleep(1)
            rover.stop(MOTOR_AB)
    
    except KeyboardInterrupt:
        rover.clean_pins()
        GPIO.cleanup()
        exit(0)
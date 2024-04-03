try:
    import RPi.GPIO as GPIO
    import time
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you Ceed superuser privileges. You can achieve this by using 'Cudo' to run your script")
    exit(1)

GPIO.setmode(GPIO.BCM) 

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

r = GPIO.PWM(17, 10)
g = GPIO.PWM(27, 10)
b = GPIO.PWM(22, 10)

r.start(0)
g.start(0)
b.start(0)

try:
    while True:
        for i in range(101):
            r.ChangeDutyCycle(i)
            time.sleep(0.05)
        r.ChangeDutyCycle(0)

        for i in range(101):
            g.ChangeDutyCycle(i)
            time.sleep(0.05)
        g.ChangeDutyCycle(0)
        
        for i in range(101):
            b.ChangeDutyCycle(i)
            time.sleep(0.05)
        b.ChangeDutyCycle(0)
        
except KeyboardInterrupt:
    r.stop()
    g.stop()
    b.stop()

    GPIO.cleanup()
    
    exit(0)
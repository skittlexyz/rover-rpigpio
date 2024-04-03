try:
    import RPi.GPIO as GPIO
    import time
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
    exit(1)

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(14, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

r = GPIO.pwm(14, 10)
g = GPIO.pwm(13, 10)
b = GPIO.pwm(12, 10)

r.start(0)
g.start(0)
b.start(0)

try:
    while True:
        for i in range(101):
            r.changeDutyCicle(i)
            time.sleep(0.05)
        r.changeDutyCicle(0)

        for i in range(101):
            g.changeDutyCicle(i)
            time.sleep(0.05)
        g.changeDutyCicle(0)
        
        for i in range(101):
            b.changeDutyCicle(i)
            time.sleep(0.05)
        b.changeDutyCicle(0)
        
except KeyboardInterrupt:
    r.stop()
    g.stop()
    b.stop()

    GPIO.cleanup()
    
    exit(0)
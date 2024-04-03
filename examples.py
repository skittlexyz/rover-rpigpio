# trying to import library
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
    exit(1)

GPIO.setmode(GPIO.BOARD) # sets the pin number system
# GPIO.setwarnings(False) # disables warning in case of another script running at the same time

# return all the changes to initial state
GPIO.cleanup()
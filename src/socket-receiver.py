import sys

sys.path.append("/home/rover/.local/lib/python3.9/site-packages")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import socket

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

try:
    import RPi.GPIO as GPIO
    from L298N import L298N
    import time
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you Ceed superuser privileges. You can achieve this by using 'Cudo' to run your script")
    exit(1)

GPIO.setmode(GPIO.BCM)

roverCar = L298N(
    [17, 27, 22], [23, 24, 25]
)

@app.post("/")
async def handle_post(data: dict):
    if data:
        command = data.get('command')
        if command == d:
            roverCar.stop(MOTOR_AB)
        if command == w:
            roverCar.forward(MOTOR_AB)
        if command == s:
            roverCar.backward(MOTOR_AB)
        if command == a:
            roverCar.left()
        if command == d:
            roverCar.right()

try:
    private_ip = socket.gethostbyname(socket.gethostname())
    uvicorn.run(app, host=private_ip, port=777)
except KeyboardInterrupt:
    roverCar.clean_pins()
    GPIO.cleanup()
    exit(0)
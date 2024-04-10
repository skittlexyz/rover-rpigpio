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

import L298N

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

@app.post("/")
async def handle_post(data: dict):
    if data:
        command = data.get('command')
        if command == d:
            rover.stop(MOTOR_AB)
        if command == w:
            rover.forward(MOTOR_AB)
        if command == s:
            rover.backward(MOTOR_AB)
        if command == a:
            rover.left()
        if command == d:
            rover.right()

try:
    private_ip = socket.gethostbyname(socket.gethostname())
    uvicorn.run(app, host=private_ip, port=777)
except KeyboardInterrupt:
    rover.clean_pins()
    GPIO.cleanup()
    exit(0)
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

from L298N import *

roverCar = L298N(
    [17, 27, 22], [23, 24, 25]
)
roverCar.change_speed(75)

@app.post("/")
async def handle_post(data: dict):
    if data:
        command = data.get('command')
        if command == 'f':
            roverCar.stop(MOTOR_AB)
        if command == 'w':
            roverCar.forward(MOTOR_AB)
        if command == 's':
            roverCar.backward(MOTOR_AB)
        if command == 'a':
            roverCar.left()
        if command == 'd':
            roverCar.right()

try:
    private_ip = "192.168."
    uvicorn.run(app, host=private_ip, port=777)
except KeyboardInterrupt:
    roverCar.clean_pins()
    exit(0)
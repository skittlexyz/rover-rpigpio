from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

import L298N

app = Flask(__name__)
CORS(app)

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

@app.route('/', methods=['POST'])
def handle_post():
    rover.change_speed(50)
    data = request.get_json()
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
        if command:
            print("Received command:", command)
            # Handle the command received from the client
            # You can add your logic here to perform actions based on the received command
            return jsonify({'message': 'Command received successfully'})
    return jsonify({'error': 'Invalid request'})

try:
    private_ip = socket.gethostbyname(socket.gethostname())
    app.run(host=private_ip, port=5000, debug=True)
except KeyboardInterrupt:
    rover.clean_pins()
    GPIO.cleanup()
    exit(0)
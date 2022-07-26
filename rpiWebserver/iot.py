import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from gpiozero import DistanceSensor
from time import sleep

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 14
led2 = 18
buzzer = 15

ledSts = 0
buzzerSts = 0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led, GPIO.LOW)
GPIO.output(buzzer, GPIO.LOW)

@app.route("/")
def index():
    
    ledSts = GPIO.input(led)
    led2Sts = GPIO.input(led)
    buzzerSts = GPIO.input(buzzer)
    dist = 0
    sensor = DistanceSensor(echo=21, trigger=20, max_distance=6.0)
    dist = sensor.distance * 100 

    templateData = {
        'led' : ledSts,
        'led2' : led2Sts,
        'buzzer' : buzzerSts,
        'distance' : dist
    }
    return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    dist = 0
    if deviceName == 'led':
        actuator = led
    if deviceName == 'led2':
        actuator = led2
    if deviceName == 'buzzer':
        actuator = buzzer
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    if deviceName == 'distance' and action == 'compute':
        sensor = DistanceSensor(echo=21, trigger=20, max_distance=6.0)
        dist = sensor.distance * 100             
        
    ledSts = GPIO.input(led)
    led2Sts = GPIO.input(led2)
    buzzerSts = GPIO.input(buzzer)

    templateData = {
        'led' : ledSts,
        'led2' : led2Sts,
        'buzzer' : buzzerSts,
        'distance' : dist,
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.91', port = 5001)
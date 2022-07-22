import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def led_run_on(x):
    GPIO.output(x, True)
    print("on", x)
    time.sleep(0.02)
    return

def led_run_off(x):
    GPIO.output(x, False)
    print("off", x)
    time.sleep(0.02)
    return

while (True):
    i=2
    for i in range(2, 14):
        led_run_on(i)
        time.sleep(0.02)
        if i == 13:
            print("beeep")
            time.sleep(1)
    for i in range(13, 1, -1):
        led_run_off(i)
        time.sleep(0.02)
   
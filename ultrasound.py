import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 4
GPIO_ECHO = 17
led = 27

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIGGER, GPIO.LOW)

def get_range():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    timeout_counter=int(time.time())
    start = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
    timeout_counter = int(time.time())
    stop = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()
    
    elapsed = stop - start
    distance = elapsed*34320
    distance = distance / 2
    return distance

while True:
    jarak = get_range()
    if jarak <= 5:
        GPIO.output(led, True)
        print("Jarak terlalu dekat!! %.2f cm"%jarak)
        time.sleep(1)
    else:
        GPIO.output(led, False)
        print("Jarak halangan di depan adalah %.2f Cm"%jarak)
        time.sleep(1)
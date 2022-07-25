import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

inpBtn = 2
GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(inpBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

statusBtn = False
inputLama = True

while True:
    statusBaru = GPIO.input(inpBtn)
    if statusBaru == False and inputLama == True:
        statusBtn = not statusBtn
        time.sleep(0.2)
    inputLama = statusBaru
    GPIO.output(3, statusBtn)

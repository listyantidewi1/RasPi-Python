import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

tunda = 0.1
value = 0
ldr = 3
led = 11
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)
def rc_time(ldr):
    count = 0
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(tunda)
    GPIO.setup(ldr, GPIO.IN)
    
    while(GPIO.input(ldr) == 0):
        count +=1
        
    return count

try:
    while True:
        print("Nilai ldr: ")
        value = rc_time(ldr)
        print(value)
        if(value >= 350000):
            print("Lights are ON")
            GPIO.output(led, True)
        if(value<350000):
            print("Lights are OFF")
            GPIO.output(led, False)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 2
led2 = 3
led3 = 4

btn = 17
ldr = 27

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(ldr, GPIO.IN)

statusBtn = False
inputLama = True

GPIO.output(led1, False)
GPIO.output(led2, False)

def rc_time(ldr):
    count = 0
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(0.5)
    GPIO.setup(ldr, GPIO.IN)
    
    while(GPIO.input(ldr)==0):
        count += 1
    
    return count


try:
    while True:
        statusBaru = GPIO.input(btn)
        #print("status baru ", statusBaru)
        
        if statusBaru == False and inputLama == True:
            statusBtn = not statusBtn
            time.sleep(0.2)
            
        inputLama = statusBaru
        
        GPIO.output(led3, statusBtn)
        if statusBtn == True:
            print("lampu ruang tamu nyala")
        else:
            print("lampu ruang tamu mati") 
        #print("status button: ", statusBtn)
        
        #print("Nilai ldr: ")
        value = rc_time(ldr)
        #print(value)
        if(value >= 3500):
            print("Lampu taman nyala")
            GPIO.output(led1, True)
            GPIO.output(led2, True)
        elif(value<2000):
            print("Lampu taman mati")
            GPIO.output(led1, False)
            GPIO.output(led2, False)
            
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
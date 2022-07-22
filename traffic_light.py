import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pos1red = 2
pos1yellow = 3
pos1green = 4

pos2red = 5
pos2yellow = 6
pos2green = 7

pos3red=8
pos3yellow=9
pos3green=10

pos4red=11
pos4yellow=12
pos4green=13

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
    

def scene1_4():
    GPIO.output(pos1red, True) #2
    GPIO.output(pos1yellow, False) #3
    GPIO.output(pos1green, False) #4
    GPIO.output(pos2red, False) #5
    GPIO.output(pos2yellow, False) #6
    GPIO.output(pos2green, True) #7
    GPIO.output(pos3red, False) #8
    GPIO.output(pos3yellow, False) #9
    GPIO.output(pos3green, True) #10
    GPIO.output(pos4red, True) #11
    GPIO.output(pos4yellow, False) #12
    GPIO.output(pos4green, False) #13
    time.sleep(5)
    return

def warning1_4():
    GPIO.output(pos1red, True) #2
    GPIO.output(pos1yellow, True) #3
    GPIO.output(pos1green, False) #4
    GPIO.output(pos2red, False) #5
    GPIO.output(pos2yellow, True) #6
    GPIO.output(pos2green, False) #7
    GPIO.output(pos3red, False) #8
    GPIO.output(pos3yellow, True) #9
    GPIO.output(pos3green, False) #10
    GPIO.output(pos4red, True) #11
    GPIO.output(pos4yellow, True) #12
    GPIO.output(pos4green, False) #13
    time.sleep(1)
    return

def warning2_3():
    GPIO.output(pos1red, False) #2
    GPIO.output(pos1yellow, True) #3
    GPIO.output(pos1green, False) #4
    GPIO.output(pos2red, True) #5
    GPIO.output(pos2yellow, True) #6
    GPIO.output(pos2green, False) #7
    GPIO.output(pos3red, True) #8
    GPIO.output(pos3yellow, True) #9
    GPIO.output(pos3green, False) #10
    GPIO.output(pos4red, False) #11
    GPIO.output(pos4yellow, True) #12
    GPIO.output(pos4green, False) #13
    time.sleep(1)
    return

def scene2_3():
    GPIO.output(pos1red, False) #2
    GPIO.output(pos1yellow, False) #3
    GPIO.output(pos1green, True) #4
    GPIO.output(pos2red, True) #5
    GPIO.output(pos2yellow, False) #6
    GPIO.output(pos2green, False) #7
    GPIO.output(pos3red, True) #8
    GPIO.output(pos3yellow, False) #9
    GPIO.output(pos3green, False) #10
    GPIO.output(pos4red, False) #11
    GPIO.output(pos4yellow, False) #12
    GPIO.output(pos4green, True) #13
    time.sleep(5)
    return

while (True):
    scene1_4()
    warning1_4()
    scene2_3()
    warning2_3()
    

    
    




    

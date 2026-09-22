import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
led=26
photo=6
GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo, GPIO.IN)
state=0
period=1.0
while True:
    GPIO.output(led, state)
    state=not state
    time.sleep(period)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
button=13
led=26
state=0
GPIO.setup(button,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
try:
    while True:
        if GPIO.input(button)==1:
            state=1
        else:
            state=0
        GPIO.output(led, state)
        time.sleep(0.2)
except KeyboardInterrupt:
     pass
finally:
    GPIO.cleanup()
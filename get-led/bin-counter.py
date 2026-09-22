import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
leds=[16,12,25,17,27,23,22,24]
GPIO.setup(leds,GPIO.OUT)
UP_PIN=9
DOWN_PIN=10
GPIO.setup(UP_PIN, GPIO.IN)
GPIO.setup(DOWN_PIN,GPIO.IN)
num=0
def dec2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
sleep_time=0.2
while True:
    if GPIO.input(UP_PIN):
        num=num+1
        print(num,dec2bin(num))
        time.sleep(sleep_time)
        GPIO.output(leds, dec2bin(num))
    elif GPIO.input(DOWN_PIN):
        num=num-1
        if num<0:
            num=255
        print(f"Число{num} , {dec2bin(num)}")
        time.sleep(sleep_time)
        GPIO.output(leds,dec2bin(num))


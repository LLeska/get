import RPi.GPIO as GPIO
import time

#const
led_pins = [24,22,23,27,17,25,12,16]
plus_pin = 9
minus_pin = 10

#var
numb = 5


#setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)
GPIO.setup(plus_pin, GPIO.IN)
GPIO.setup(minus_pin, GPIO.IN)
GPIO.output(led_pins, 0)

#main loop
while True:
    plus_in = GPIO.input(plus_pin)
    minus_in = GPIO.input(minus_pin)
    if plus_in and minus_in: 
        numb = 2**8-1
    elif plus_in and numb < 2**8-1: 
        numb += 1
    elif minus_in and numb > 0: 
        numb -= 1


    bin_numb = bin(numb)[2:].zfill(8)



    for i in range(1, 9):
        GPIO.output(led_pins[-i], int(bin_numb[i-1]))
    time.sleep(0.2)
GPIO.cleanup()

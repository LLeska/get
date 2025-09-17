import RPi.GPIO as GPIO
import time

#const
led_pin = 26
button_pin = 13

#var
led_state = False

#setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

#main loop
while True:
    if GPIO.input(button_pin):
        GPIO.output(led_pin, led_state)
        if led_state: led_state = False
        else: led_state = True
        time.sleep(0.2)

GPIO.cleanup()

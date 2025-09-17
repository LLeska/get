import RPi.GPIO as GPIO
import time

#const
led_pin = 26
blink_period = 1.0

#var
led_state = False

#setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

#main loop
while True:
    GPIO.output(led_pin, led_state)
    if led_state: led_state = False
    else: led_state = True
    time.sleep(blink_period)

GPIO.cleanup()

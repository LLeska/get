import RPi.GPIO as GPIO
import time

#const
led_pins = [24,22,23,27,17,25,12,16]
button_pin = 13

#var
light_time = 0.2

#setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)

GPIO.output(led_pins, 0)

#main loop
while True:
    for led_pin in led_pins:
        GPIO.output(led_pin, 1)
        time.sleep(light_time)
        GPIO.output(led_pin, 0)
    for led_pin in reversed(led_pins):
        GPIO.output(led_pin, 1)
        time.sleep(light_time)
        GPIO.output(led_pin, 0)
GPIO.cleanup()

import RPi.GPIO as GPIO
import time

#const
led_pin = 26
phototransistor_pin = 6

#var


#setup
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(phototransistor_pin, GPIO.IN)

#main loop
while True:
    GPIO.output(led_pin, (not GPIO.input(phototransistor_pin)))
    time.sleep(0.2)

GPIO.cleanup()

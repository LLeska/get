import RPi.GPIO as GPIO
import r2r_dac 
from time import sleep


class R2R_ACD:
    def __init__(self, gpio_bits, dynamic_range: float,comp_pin: int, verbose: bool = False):
        self.__dac = r2r_dac.R2R_DAC(gpio_bits, dynamic_range, True)
        self.__comp_pin = comp_pin

        GPIO.setup(comp_pin, GPIO.IN)

    def deinit(self) -> None:
        self.__dac.deinit()

    def bit_finder(self) -> float:
        l = 0
        r = 255
        while( r-l > 1):
            self.__dac.set_number((r+l)//2)
            sleep(0.005)
            if(GPIO.input(self.__comp_pin)):
                r = (r+l)//2
            else:
                l = (r+l)//2
        return ((r+l)/510)*self.__dac.get_dynamic_range()

    def up_fnder(self) -> float:
        n = -1
        while(GPIO.input(self.__comp_pin) or n < 256):
            n += 1
            self.__dac.set_number(n)
            sleep(0.005)
        if n != 256: return (n/255) * self.__dac.get_dynamic_range()
        return self.__dac.get_dynamic_range()


if __name__ == "__main__":
    dynamic_range = 3
    gpio_bits = [11,25,12,13,16,19,20,26]
    gpio_bits = gpio_bits[::-1]
    comp_pin = 21
    adc = R2R_ACD(gpio_bits, dynamic_range,comp_pin, True)
    try:
        while True:
            print(adc.bit_finder())
    finally:
        adc.deinit()

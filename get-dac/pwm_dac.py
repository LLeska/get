import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin: int, pwm_frequency: int, dynamic_range: float, verbose: bool = False):
        self.__gpio_pin = gpio_pin
        self.__pwm_frequency = pwm_frequency 
        self.__dynamic_range = dynamic_range 
        self.__verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__gpio_pin, GPIO.OUT, initial = 0)

        self.__pwm = GPIO.PWM(self.__gpio_pin, self.__pwm_frequency)
        self.__pwm.start(0)
        


    def deinit(self):
        GPIO.output(self.__gpio_pin, 0)
        GPIO.cleanup()


    def set_voltage(self, voltage: float) -> None:
        if not (0.0 <= voltage <= self.__dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.__dynamic_range:.2f} В)")
            return

        self.__pwm.ChangeDutyCycle((voltage / self.__dynamic_range)*100)



if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 1000, 3.285, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
            

    finally:
        dac.deinit()

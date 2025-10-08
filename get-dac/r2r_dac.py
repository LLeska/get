import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits: list[int], dynamic_range: float, verbose: bool = False):
        self.__gpio_bits = gpio_bits
        self.__dynamic_range = dynamic_range
        self.__verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.__gpio_bits, 0)
        GPIO.cleanup()


    def set_number(self, num: int) -> None:
        bin_numb = bin(num)[2:].zfill(8)

        for i in range(1, 9):
            GPIO.output(self.__gpio_bits[-i], int(bin_numb[i-1]))


    def set_voltage(self, voltage: float) -> None:
        if not (0.0 <= voltage <= self.__dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.__dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.set_number(0)
            return 

        self.set_number(int(voltage / self.__dynamic_range * 255))



if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

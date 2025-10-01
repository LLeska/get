import RPi.GPIO as GPIO


dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.183


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(num):
    bin_numb = bin(num)[2:].zfill(8)

    for i in range(1, 9):
        GPIO.output(dac_bits[-i], int(bin_numb[i-1]))


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()

import smbus


class MCP4725:
    def __init__(self, dynamic_range: float, address: str=0x61, verbose: bool = True):
        self.__bus = smbus.SMBus(1)

        self.__address = address
        self.__wm = 0x00
        self.__pds = 0x00

        self.__verbose = verbose
        self.__dynamic_range = dynamic_range

    def deinit(self):
        self.__bus.close()

    def set_number(self, number: int) -> None:
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 4095):
            print("Число выходит за разраядность MCP4752 (12 бит)")
            return

        first_byte = self.__wm | self.__pds | number >> 8
        second_byte = number & 0xFF
        self.__bus.write_byte_data(self.__address, first_byte, second_byte)

        if self.__verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.__address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage: float) -> None:
        if not (0 <= voltage <= self.__dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.__dynamic_range:.2f} В)")
            return
        self.set_number(int((voltage/self.__dynamic_range)*4095))

    def set_number_8_bit(self, number: int) -> None:
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 255):
            print("Число выходит за разраядность MCP4752 (12 бит)")
            return

        number = 4095 * number / 255

        first_byte = self.__wm | self.__pds | number >> 8
        second_byte = number & 0xFF
        self.__bus.write_byte_data(self.__address, first_byte, second_byte)

        if self.__verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.__address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage_8_bit(self, voltage: float) -> None:
        if not (0 <= voltage <= self.__dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.__dynamic_range:.2f} В)")
            return
        self.set_number_8_bit(int((voltage/self.__dynamic_range)*255))        


if __name__ == "__main__":
    try:
        mcp = MCP4725(5.17)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                mcp.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
            

    finally:
        mcp.deinit()

import smbus

dynamic_range = 3.287

class MCP3021:
    def __init__(self, dynamic_range: float, address: bool=0x4d, verbose: bool = True):
        self.__bus = smbus.SMBus(1) 
        self.__address = address
        self.__wm = 0x00
        
        self.__pds = 0x00

        self.__verbose = verbose
        self.__dynamic_range = dynamic_range

    def read(self) -> float:
        res = self.__bus.read_i2c_block_data(self.__address, 0, 2)
        return ((((res[0] & 0x0F) << 6)|(res[1]>>2))/650)*self.__dynamic_range

    def deinit(self) -> None:
        self.__bus.close()
           
           
if __name__ == "__main__":
    from time import sleep
    try:
        acd = MCP3021(dynamic_range)
        while True:
            sleep(0.005)
            print(acd.read())
    finally:
        acd.deinit()

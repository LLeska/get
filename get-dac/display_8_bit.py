import r2r_dac
import mcp4725_driver
from time import time 
import signal_generator


class DISPLAY_8_BIT():
    def __init__(self,
                 sampling_frequency: int = 1000, # Hz
                 r2r_pins = [16, 20, 21, 25, 26, 17, 27, 22],
                 r2r_dynamic_range: float = 3.183, # V
                 mcp_dynamic_range: float = 5.17): # v
        self.__sampling_frequency = sampling_frequency
        self.__r2r_pins = r2r_pins
        self.__r2r_dynamic_range = r2r_dynamic_range
        self.__mcp_dynamic_range = mcp_dynamic_range

        self.__dac_r2r = r2r_dac.R2R_DAC(self.__r2r_pins, self.__r2r_dynamic_range)
        self.__dac_mcp = mcp4725_driver.MCP4725(self.__mcp_dynamic_range)

    def matrix(self, pix_arr):
        t0 = time()
        for i in range(256):
                for j in range(256):
                    if pix_arr[i][j] != 0:
                        self.__dac_r2r.set_number(i)
                        self.__dac_mcp.set_number_8_bit(j)
        signal_generator.wait_for_sampling_period(self.__sampling_frequency, time() - t0)

    def deinit(self):
        self.__dac_mcp.deinit()
        self.__dac_r2r.deinit()
        
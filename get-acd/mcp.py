import mcp_3021_adc
from time import time
import adc_plot


if __name__ == "__main__":
    dynamic_range = 5
    acd = mcp_3021_adc.MCP3021(dynamic_range)
    times = []
    mess = []
    experement_time = 5

    try:
        t0 = time()

        while(time() - t0 < experement_time):
            mes = acd.read()
            t1 = time()
            times.append(t1-t0)
            mess.append(mes)
        if len(times) == 0:
            times = [0]
            mess = [0]
        adc_plot.plot_voltage_vs_time(times, mess)
    finally:
        acd.deinit()

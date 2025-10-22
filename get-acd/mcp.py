import mcp_3021_adc
from time import time
import adc_plot


if __name__ == "__main__":
    dynamic_range = 5
    acd = mcp_3021_adc.MCP3021(dynamic_range)
    times = []
    mess = []

    experement_time = 100

    try:
        t0 = time()
        while(t0-time() > experement_time):
            mes = acd.read()
            t1 = time()
            times.append(t1-t0)
            mess.append(mes)
        adc_plot.plot_voltage_vs_time(time, mess)
        adc_plot.plot_sampling_period_hist(time)
    finally:
        acd.deinit()

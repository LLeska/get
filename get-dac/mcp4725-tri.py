import mcp4725_driver
import signal_generator
import time



signal_frequency = 10
sampling_frequency = 1000
dynamic_range = 3.285



if __name__ == "__main__":
    try:
        dac = mcp4725_driver.MCP4725(dynamic_range)
        t0 = time.time_ns
        while True:
            try:
                signal_generator.wait_for_sampling_period(sampling_frequency)
                dac.set_voltage(signal_generator.get_tri_wave_amplitude(signal_frequency ,time.time_ns-t0)*dynamic_range)
            except ValueError:
                print(ValueError)
    finally:
        dac.deinit()
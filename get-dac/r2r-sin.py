import signal_generator
import r2r_dac
import time


signal_frequency = 10
sampling_frequency = 1000
r2r_pins = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.183


if __name__ == "__main__":
    try:
        dac = r2r_dac.R2R_DAC(r2r_pins, dynamic_range)
        t0 = time.time_ns
        while True:
            try:
                signal_generator.wait_for_sampling_period(sampling_frequency)
                dac.set_number(signal_generator.get_sin_wave_amplitude(signal_frequency ,time.time_ns-t0)*255)
            except ValueError:
                print(ValueError)
    finally:
        dac.deinit()
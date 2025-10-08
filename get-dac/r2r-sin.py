import signal_generator
import r2r_dac
import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        dac = r2r_dac.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183)
        t0 = time.time_ns
        while True:
            try:
                dac.set_number(signal_generator.get_sin_wave_amplitude(signal_frequency ,time.time_ns-t0)*255)
            except ValueError:
                print(ValueError)
    finally:
        dac.deinit()
import pwm_dac
import signal_generator
import time


signal_frequency = 10
sampling_frequency = 1000
pwm_pin = 12
dynamic_range = 3.285



if __name__ == "__main__":
    try:
        dac = pwm_dac.PWM_DAC(pwm_pin, sampling_frequency, dynamic_range)
        t0 = time.time_ns
        while True:
            try:
                dac.set_voltage(signal_generator.get_tri_wave_amplitude(signal_frequency ,time.time_ns-t0)*dynamic_range)
            except ValueError:
                print(ValueError)
    finally:
        dac.deinit()
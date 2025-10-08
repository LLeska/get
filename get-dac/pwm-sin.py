import pwm_dac
import signal_generator
import time


signal_frequency = 10
sampling_frequency = 100
pwm_pin = 12
dynamic_range = 3



if __name__ == "__main__":
    try:
        dac = pwm_dac.PWM_DAC(pwm_pin, sampling_frequency, dynamic_range)
        t0 = time.time()
        while True:
            try:
                dac.set_voltage(signal_generator.get_sin_wave_amplitude(signal_frequency ,time.time())*dynamic_range)
            except ValueError:
                print(ValueError)
    finally:
        dac.deinit()
from math import sin, pi
from time import sleep


def get_sin_wave_amplitude(freq: int, time: int) -> float: #return amplitude coefficient in [0;1]
    return (sin(2*pi*freq*time) + 1.0) / 2.0


def wait_for_sampling_period(sampling_frequency: int) -> None: #wait 1 sampling period
    sleep(1000.0/sampling_frequency)
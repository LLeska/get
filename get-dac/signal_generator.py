from math import sin, asin
from time import sleep


def get_sin_wave_amplitude(freq: int, time: float) -> float: #return amplitude coefficient in [0;1]
    return (1 - sin(2*3.14*freq*time)) * 0.5

def get_tri_wave_amplitude(freq:int, time: float) -> float:
    return ((- 2.0 / 3.14) * asin(sin(2*3.14*freq*time)) + 1) / 2


def wait_for_sampling_period(sampling_frequency: int) -> None: #wait 1 sampling period
    sleep(1/sampling_frequency)
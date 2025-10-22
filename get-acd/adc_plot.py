from matplotlib import pyplot

def plot_voltage_vs_time(time, voltage):
    pyplot.figure(figsize=(10,6))
    pyplot.plot(time, voltage)
    pyplot.title("Зависимость напряжения от времени")
    pyplot.xlabel("Время, с")
    pyplot.ylabel("Напряжение, В")
    pyplot.xlim(min(time), max(time))
    pyplot.ylim(0, max(voltage) * 1.1)
    pyplot.grid(True)
    pyplot.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        sampling_periods.append(time[i] - time[i-1])
    
    pyplot.figure(figsize=(10,6))
    pyplot.hist(sampling_periods)
    pyplot.title("Распределение периодов измерений")
    pyplot.xlabel("Период, с")
    pyplot.ylabel("Количество измерений")
    pyplot.xlim(0, 0.06)
    pyplot.grid(True)
    pyplot.show()
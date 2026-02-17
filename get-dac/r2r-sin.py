import r2r_dac as r2r
import signal_generator as sg
import RPi.GPIO as GPIO
import time

amplitude = 3.29
signal_frequency = 10
sampling_frequency = 1000
t = 0

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], float(3.29), True)
    dacb = [16, 20, 21, 25, 26, 17, 27, 22]
    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency, t)
            print(voltage)
            dac.set_voltage(voltage*amplitude)

            sg.wait_for_sampling_period(sampling_frequency)
            t = time.time()
        except ValueError:
            print("Вы ввели на число. Попробуйте ещё раз\n")

finally:
    dac.deinit()
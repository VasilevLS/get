import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin,pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    
    def set_number(self, number):
        print(number)
        number = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_pin, number)
        print(number)
    
    def set_voltage(self, votlage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            return 0
        self.set_number(int(voltage / self.dynamic_range * 255))

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12,500, float(3.146), True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели на число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
fot = 6
GPIO.setup(fot, GPIO.IN)
state = 0
while True:
    if GPIO.input(fot):
        GPIO.output(led, 0)
    else:
        GPIO.output(led, 1)

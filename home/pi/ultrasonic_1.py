import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2e-6)
GPIO.output(TRIG, True)
time.sleep(1e-5)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
	pulse_start = time.time()

while GPIO.input(ECHO) == 1:
	pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

# distance = pulse_duration * 17150
# distance = round (distance,2)
# print(distance)
print(pulse_duration)
GPIO.cleanup()
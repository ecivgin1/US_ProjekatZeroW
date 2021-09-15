import RPi.GPIO as GPIO
import board
import digitalio
import time
from threading import Thread

def configure_buzzer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    buzzer = 17
    GPIO.setup(buzzer, GPIO.OUT)
    freq = GPIO.PWM(buzzer,100)

    return freq

freq = configure_buzzer()

def zvuk(level):    
    freq.start(100)
    time.sleep(0.15)
    freq.stop()
    if level == 4:
        time.sleep(0.03)
    else:
        time.sleep(0.65 - level*0.15)

def prvi_t():
    while True:
        print("Prvi")
        time.sleep(10)
        # zvuk(1)

# def drugi_t():
#     while True:
#         print("Drugi")
#         time.sleep(2)

_thread.start_new_thread(prvi_t, ())
_thread.start_new_thread(drugi_t, ())

for i in range (10):
    # print("hihi")
    time.sleep(1)
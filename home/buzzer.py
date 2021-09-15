import time
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 17

GPIO.setup(buzzer, GPIO.OUT)
freq = GPIO.PWM(buzzer,1/0.75)

nivo = 4

while True:
    # freq.ChangeFrequency(0.5)
    # freq.start(35)
    # time.sleep(5)
    # freq.stop()

    # freq.ChangeFrequency(1)
    # freq.start(50)
    # time.sleep(5)
    # freq.stop()

    # freq.ChangeFrequency(1.5)
    # freq.start(65)
    # time.sleep(5)
    # freq.stop()
    if nivo == 4:
        freq.ChangeFrequency(1/0.18)
        freq.start(83)
    if nivo == 3:
        freq.ChangeFrequency(1/0.35)
        freq.start(43)
    if nivo == 2:
        freq.ChangeFrequency(2)
        freq.start(30)
    if nivo == 1:
        freq.ChangeFrequency(1/0.65)
        freq.start(23)
    if nivo == 0:
        freq.ChangeFrequency(0.5)
        freq.start(0)
        print("nula")
    time.sleep(5)
    freq.stop()
    break



#level 2
# while True:
#     freq.start(100)
#     time.sleep(0.15)
#     freq.stop()
#     time.sleep(0.35)

#level 3
# while True:
#     freq.start(100)
#     time.sleep(0.15)
#     freq.stop()
#     time.sleep(0.2)

#level 4
# while True:
#     freq.start(100)
#     time.sleep(0.15)
#     freq.stop()
#     time.sleep(0.03)

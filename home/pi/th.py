import logging
import threading
import time
import RPi.GPIO as GPIO
import board
import digitalio

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

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

def thread1():
    for i in range(10):
        print("T1: ", i)
        zvuk(1)
        # time.sleep(1)

def thread2():
    print("T2: pocetak")
    time.sleep(2.5)
    print("T2: kraj")

if __name__ == "__main__":
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()

    # threads = list()
    # for index in range(3):
    #     logging.info("Main    : create and start thread %d.", index)
         
    #     x = threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index)
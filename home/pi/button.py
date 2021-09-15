import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

i = 0
while True: # Run forever
    if GPIO.input(37) == GPIO.HIGH:
        # print("Button was pushed!")
        print(i)
        i += 1
        break

print("upaljeno")
time.sleep(2)


while True:
    if GPIO.input(37) == GPIO.HIGH:
        break
    
print("izgaseno")

# import time

# start = time.time()
# print("hello")
# time.sleep(1)
# end = time.time()
# print(end - start)


# channel = 37

# GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# # while GPIO.input(channel) == GPIO.LOW:
# #     time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

# def my_callback(channel):
#     print('This is a edge event callback function!')
#     print('Edge detected on channel %s'%channel)
#     print('This is run in a different thread to your main program')

# GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)  # add rising edge detection on a channel
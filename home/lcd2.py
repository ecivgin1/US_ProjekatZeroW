from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
lcd = CharLCD(pin_rs=37, pin_e=35, pins_data=[33,31,29,23])
lcd.write_string(u'Hello World!')

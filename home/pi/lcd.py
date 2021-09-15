import digitalio
import board
import sys
import RPi.GPIO as GPIO
import time
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import

def configure_display():
    # Configuration for CS and DC pins (these are PiTFT defaults):
    cs_pin = digitalio.DigitalInOut(board.CE0)
    dc_pin = digitalio.DigitalInOut(board.D25)
    reset_pin = digitalio.DigitalInOut(board.D24)

    # Config for display baudrate (default max is 24mhz):
    BAUDRATE = 24000000

    # Setup SPI bus using hardware SPI:
    spi = board.SPI()

    # Create the display:
    disp = st7735.ST7735R(
        spi,
        rotation=270,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )
    return disp

def configure_buzzer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    buzzer = 17
    GPIO.setup(buzzer, GPIO.OUT)
    freq = GPIO.PWM(buzzer,100)

    return freq

disp = configure_display()
freq = configure_buzzer()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height

image = Image.open("AutoResizeLCD.png").convert("RGB")

background = Image.new('RGB', (160, 128), (0, 0, 0))
offset = (10, 35)
background.paste(image, offset)

def lines(level):
    if level == 4:
        lines(3)
        drawText.line((115, 40, 115, 80), fill = (0, 0, 255), width = 4)
        drawText.line((110, 35, 115, 40), fill = (0, 0, 255), width = 4)
        drawText.line((110, 85, 115, 80), fill = (0, 0, 255), width = 4)
    if level == 3:
        lines(2)
        drawText.line((125, 40, 125, 80), fill = (0, 85, 255), width = 3)
        drawText.line((115, 30, 125, 40), fill = (0, 85, 255), width = 3)
        drawText.line((115, 90, 125, 80), fill = (0, 85, 255), width = 3)
    if level == 2:
        lines(1)
        drawText.line((135, 40, 135, 80), fill = (0, 170, 255), width = 2)
        drawText.line((120, 25, 135, 40), fill = (0, 170, 255), width = 2)
        drawText.line((120, 95, 135, 80), fill = (0, 170, 255), width = 2)
    if level == 1:
        drawText.line((145, 40, 145, 80), fill = (0, 255, 255), width = 1)
        drawText.line((125, 20, 145, 40), fill = (0, 255, 255), width = 1)
        drawText.line((125, 100, 145, 80), fill = (0, 255, 255), width = 1)

def zvuk(level):    
    freq.start(100)
    time.sleep(0.15)
    freq.stop()
    if level == 4:
        time.sleep(0.03)
    else:
        time.sleep(0.65 - level*0.15)
    
drawText = ImageDraw.Draw(background)

FONTSIZE = 13
font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
text = "Check Surroundings For Safety"
(font_width, font_height) = font.getsize(text)

px, py = 0.5, 1.0
drawText.text(
    (px*(width - font_width), py*(height - font_height)),
    text,
    font=font,
    fill=(255, 255, 255),
)

def senzor(vrijednost):
    if vrijednost <= 150 and vrijednost > 100:
        return 1
    elif vrijednost <= 100 and vrijednost > 60:
        return 2
    elif vrijednost <= 60 and vrijednost > 25:
        return 3
    elif vrijednost <= 25 and vrijednost >= 0:
        return 4
    else:
        return 0

# ocitanje = ultrasonic.read()
ocitanje = 140
nivo_stari = senzor(ocitanje)
lines(nivo_stari)
disp.image(background)


for i in range (20):
    ocitanje = 70
    nivo = senzor(ocitanje)
    zvuk(nivo)
    if nivo != nivo_stari:
        lines(nivo)
        disp.image(background)
    nivo_stari = nivo
for i in range (10):
    ocitanje = 40
    nivo = senzor(ocitanje)
    zvuk(nivo)
    if nivo != nivo_stari:
        lines(nivo)
        disp.image(background)
    nivo_stari = nivo

# upaljen = False

# def upali_kod():
#     while upaljen:
#         if GPIO.input(26) == GPIO.HIGH:
#             upaljen = not upaljen
#             break
#         ocitanje = 10
#         nivo = senzor(ocitanje)
#         zvuk(nivo)
#         if nivo != nivo_stari:
#             lines(nivo)
#             disp.image(background)
#         nivo_stari = nivo

# while True:
for i in range (20):
    ocitanje = 10
    nivo = senzor(ocitanje)
    zvuk(nivo)
    if nivo != nivo_stari:
        lines(nivo)
        disp.image(background)
    nivo_stari = nivo

# GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# while True:
#     print("u petlji")
#     if GPIO.input(26) == GPIO.HIGH:
#         print("pritisnut")
#         upaljen = not upaljen
#         time.sleep(2)
#         upali_kod()
    

    

# disp.image(background)
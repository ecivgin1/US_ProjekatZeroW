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

# def configure_buzzer():
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BCM)

#     buzzer = 17
#     GPIO.setup(buzzer, GPIO.OUT)
#     freq = GPIO.PWM(buzzer,100)

#     return freq

disp = configure_display()
# freq = configure_buzzer()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height

image = Image.open("UNSA10.jpg").convert("RGB")

background_prvi = Image.new('RGB', (160, 128), (255, 255, 255))
offset = (25, 9)
background_prvi.paste(image, offset)
disp.image(background_prvi)
time.sleep(2)
image = Image.open("ETF3.jpg").convert("RGB")
background_prvi.paste(image, offset)
time.sleep(2)
disp.image(background_prvi)

def napisi_tekst(text, px, py):
    drawText.text(
        (px*(width - font_width), py*(height - font_height)),
        text,
        font=font,
        fill=(255, 255, 255),
    )

#---NAZIV PROJEKTA---
background = Image.new('RGB', (160, 128), (0, 0, 0))

FONTSIZE = 20
font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
text = "Ugradbeni sistemi:"
(font_width, font_height) = font.getsize(text)

drawText = ImageDraw.Draw(background)
px, py = 0.6, 0.1
napisi_tekst(text, px, py)

FONTSIZE = 15
font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
(font_width, font_height) = font.getsize(text)

text = "Sistem za asistenciju"
px, py = 0.3, 0.4
napisi_tekst(text, px, py)

text = "prilikom parkiranja"
px, py = 0.4, 0.55
napisi_tekst(text, px, py)

text = "automobila"
px, py = 1.0, 0.7
napisi_tekst(text, px, py)

time.sleep(2)
disp.image(background)


#---Imena ucesnika---
background = Image.new('RGB', (160, 128), (0, 0, 0))
FONTSIZE = 15
font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
text = "Hamza Begic"
(font_width, font_height) = font.getsize(text)

drawText = ImageDraw.Draw(background)
px, py = 0.5, 0.3
napisi_tekst(text, px, py)

text = "Muhamed Borovac"
px, py = 0.35, 0.5
napisi_tekst(text, px, py)

text = "Eldar Čivgin"
px, py = 0.5, 0.7
napisi_tekst(text, px, py)

time.sleep(2)
disp.image(background)


#---Meni za pocetak---
background = Image.new('RGB', (160, 128), (0, 0, 0))
FONTSIZE = 15
font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
text = "Kako bi ste pokrenuli"
(font_width, font_height) = font.getsize(text)

drawText = ImageDraw.Draw(background)
px, py = 0.55, 0.1
napisi_tekst(text, px, py)

text = "sistem za asistenciju"
px, py = 0.45, 0.25
napisi_tekst(text, px, py)

text = "prilikom parkiranja,"
px, py = 0.6, 0.4
napisi_tekst(text, px, py)

text = "pritisnite taster!"
px, py = 0.9, 0.55
napisi_tekst(text, px, py)

offset = (50, 90)
image = Image.open("Start.jpg").convert("RGB")
background.paste(image, offset)

time.sleep(2)
disp.image(background)
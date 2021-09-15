import digitalio
import board
import sys
import RPi.GPIO as GPIO
import time
import socket
import threading
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
    image = Image.open("AutoResizeLCD.png").convert("RGB")
    background = Image.new('RGB', (160, 128), (0, 0, 0))
    drawText = ImageDraw.Draw(background)
    offset = (10, 35)
    background.paste(image, offset)
    FONTSIZE = 12
    font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
    text = "Check Surroundings For Safety"
    # napisi_tekst(text, 0.0, 1.0)
    drawText.text(
        (0.0, 1.0),
        text,
        font=font,
        fill=(255, 255, 255),
    )
    if level == 4:
        # lines(3)
        drawText.line((115, 40, 115, 80), fill = (0, 0, 255), width = 4)
        drawText.line((110, 35, 115, 40), fill = (0, 0, 255), width = 4)
        drawText.line((110, 85, 115, 80), fill = (0, 0, 255), width = 4)

        drawText.line((125, 40, 125, 80), fill = (0, 85, 255), width = 3)
        drawText.line((115, 30, 125, 40), fill = (0, 85, 255), width = 3)
        drawText.line((115, 90, 125, 80), fill = (0, 85, 255), width = 3)

        drawText.line((135, 40, 135, 80), fill = (0, 170, 255), width = 2)
        drawText.line((120, 25, 135, 40), fill = (0, 170, 255), width = 2)
        drawText.line((120, 95, 135, 80), fill = (0, 170, 255), width = 2)

        drawText.line((145, 40, 145, 80), fill = (0, 255, 255), width = 1)
        drawText.line((125, 20, 145, 40), fill = (0, 255, 255), width = 1)
        drawText.line((125, 100, 145, 80), fill = (0, 255, 255), width = 1)
    if level == 3:
        # lines(2)
        drawText.line((125, 40, 125, 80), fill = (0, 85, 255), width = 3)
        drawText.line((115, 30, 125, 40), fill = (0, 85, 255), width = 3)
        drawText.line((115, 90, 125, 80), fill = (0, 85, 255), width = 3)

        drawText.line((135, 40, 135, 80), fill = (0, 170, 255), width = 2)
        drawText.line((120, 25, 135, 40), fill = (0, 170, 255), width = 2)
        drawText.line((120, 95, 135, 80), fill = (0, 170, 255), width = 2)

        drawText.line((145, 40, 145, 80), fill = (0, 255, 255), width = 1)
        drawText.line((125, 20, 145, 40), fill = (0, 255, 255), width = 1)
        drawText.line((125, 100, 145, 80), fill = (0, 255, 255), width = 1)
    if level == 2:
        # lines(1)
        drawText.line((135, 40, 135, 80), fill = (0, 170, 255), width = 2)
        drawText.line((120, 25, 135, 40), fill = (0, 170, 255), width = 2)
        drawText.line((120, 95, 135, 80), fill = (0, 170, 255), width = 2)

        drawText.line((145, 40, 145, 80), fill = (0, 255, 255), width = 1)
        drawText.line((125, 20, 145, 40), fill = (0, 255, 255), width = 1)
        drawText.line((125, 100, 145, 80), fill = (0, 255, 255), width = 1)
    if level == 1:
        print("tu sam")
        drawText.line((145, 40, 145, 80), fill = (0, 255, 255), width = 1)
        drawText.line((125, 20, 145, 40), fill = (0, 255, 255), width = 1)
        drawText.line((125, 100, 145, 80), fill = (0, 255, 255), width = 1)
    # disp.image(background)
    return background

def zvuk2(D, T):
    freq.ChangeFrequency(D)
    freq.start(T)


def zvuk(level):    
    # freq.start(level*0.25)
    freq.start(100)
    time.sleep(0.45)
    freq.stop()
    # if level == 4:
    #     time.sleep(0.03)
    # else:
    #     time.sleep(0.65 - level*0.15)
    
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
# lines(nivo_stari)
# disp.image(background)

#---UVOD LCDa---

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

#---KRAJ UVODA LCDa---

# for i in range (20):
#     ocitanje = 70
#     nivo = senzor(ocitanje)
#     zvuk(nivo)
#     if nivo != nivo_stari:
#         lines(nivo)
#         disp.image(background)
#     nivo_stari = nivo
# for i in range (10):
#     ocitanje = 40
#     nivo = senzor(ocitanje)
#     zvuk(nivo)
#     if nivo != nivo_stari:
#         lines(nivo)
#         disp.image(background)
#     nivo_stari = nivo

def uspostavi_komunikaciju():
    UDP_IP = "192.168.43.237"
    UDP_PORT = 6677

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    return sock

pritisnut = False

def upali_kod(upaljen, nivo_old, background_novi, drawText_novi, sock):
    # D_curr, T_curr = 0, 0
    while upaljen:
        if GPIO.input(26) == GPIO.HIGH:
            upaljen = not upaljen
            freq.stop()
            #---OPET MENU SCREEN---

            #---Meni za pocetak---
            background_novi = Image.new('RGB', (160, 128), (0, 0, 0))
            FONTSIZE = 15
            font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
            text = "Kako bi ste pokrenuli"
            (font_width, font_height) = font.getsize(text)

            drawText_novi = ImageDraw.Draw(background_novi)
            px, py = 0.55, 0.1
            drawText_novi.text(
                (px*(width - font_width), py*(height - font_height)),
                text,
                font=font,
                fill=(255, 255, 255),
            )
            # napisi_tekst(text, px, py)

            text = "sistem za asistenciju"
            px, py = 0.45, 0.25
            drawText_novi.text(
                (px*(width - font_width), py*(height - font_height)),
                text,
                font=font,
                fill=(255, 255, 255),
            )
            # napisi_tekst(text, px, py)

            text = "prilikom parkiranja,"
            px, py = 0.6, 0.4
            drawText_novi.text(
                (px*(width - font_width), py*(height - font_height)),
                text,
                font=font,
                fill=(255, 255, 255),
            )
            # napisi_tekst(text, px, py)

            text = "pritisnite taster!"
            px, py = 0.9, 0.55
            drawText_novi.text(
                (px*(width - font_width), py*(height - font_height)),
                text,
                font=font,
                fill=(255, 255, 255),
            )
            # napisi_tekst(text, px, py)

            offset = (50, 90)
            image = Image.open("Start.jpg").convert("RGB")
            background_novi.paste(image, offset)

            time.sleep(1)
            disp.image(background_novi)

            #---KRAJ OPET MENU SCREENA---
            break
        

        data, addr = sock.recvfrom(3)
        string = str(data)
        temp = string[2:len(string)-1]
        # print(float(temp))

        ocitanje = float(temp)
        print(temp)
        nivo = senzor(ocitanje)
        # t1 = threading.Thread(target=zvuk, args=(ocitanje,))
        # print(nivo_old)
        if nivo != nivo_old:
            if nivo == 4:
                freq.ChangeFrequency(5.555)
                freq.start(83)
            if nivo == 3:
                freq.ChangeFrequency(2.857)
                freq.start(43)
            if nivo == 2:
                freq.ChangeFrequency(2)
                freq.start(30)
            if nivo == 1:
                freq.ChangeFrequency(1.538)
                freq.start(23)
            if nivo == 0:
                freq.ChangeFrequency(0.5)
                freq.start(0)
            # drawText = ImageDraw.Draw(background)
            background = lines(nivo)
            disp.image(background)
        # zvuk(nivo)
        # t1.start()
        nivo_old = nivo
    return upaljen

# while True:
# for i in range (20):
#     ocitanje = 10
#     nivo = senzor(ocitanje)
#     zvuk(nivo)
#     if nivo != nivo_stari:
#         lines(nivo)
#         disp.image(background)
#     nivo_stari = nivo

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sock = uspostavi_komunikaciju()

print(nivo_stari)
while True:
    # print("u petlji")
    if GPIO.input(26) == GPIO.HIGH:
        time.sleep(1)
        # image = Image.open("AutoResizeLCD.png").convert("RGB")
        # background = Image.new('RGB', (160, 128), (0, 0, 0))
        # drawText = ImageDraw.Draw(background)
        # FONTSIZE = 12
        # font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)
        # text = "Check Surroundings For Safety"
        # napisi_tekst(text, 0.0, 1.0)
        # offset = (10, 35)
        # background.paste(image, offset)

        print("pritisnut")
        pritisnut = not pritisnut
        pritisnut = upali_kod(pritisnut, nivo_stari, background, drawText, sock)
        # pritisnut = not pritisnut
    

    

# disp.image(background)
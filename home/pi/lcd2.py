import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import


FONTSIZE = 13

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
        rotation=270,  # 2.2", 2.4", 2.8", 3.2" ILI9341
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )
    return disp

disp = configure_display()


# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/home/pi/PixelOperator.ttf", FONTSIZE)

# Get drawing object to draw on image.
text = "Check Surrounding For Safety"
(font_width, font_height) = font.getsize(text)
# draw.text(
#     (width // 2 - font_width // 2, height // 2 - font_height // 2),
#     text,
#     font=font,
#     fill=(255, 255, 0),
# )

# Draw a black filled box to clear the image.
# draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
# disp.image(image)

# image = Image.open("AutoResizeLCD.png").convert("RGB")

# Scale the image to the smaller screen dimension
# image_ratio = image.width / image.height
# screen_ratio = width / height
# scale = 0.4
# if screen_ratio < image_ratio:
#     scaled_width = image.width * height // image.height
#     scaled_height = height
# else:
#     scaled_width = width
#     scaled_height = image.height * width // image.width
# image = image.resize((int(scale*scaled_width), int(scale*scaled_height)), Image.BICUBIC)

# Crop and center the image
# x = scaled_width // 2 - width // 2
# y = scaled_height // 2 - height // 2
# y = scaled_height/2
# print(y)
# print(y + height)
# image = image.crop((x-55, y-30, x-55 + width, y-30 + height))
# image = image.crop((10, 40, 110, 90))
# disp.image(image)

# Display image.
disp.image(image)

image = Image.open("AutoResizeLCD.png").convert("RGB")

background = Image.new('RGB', (160, 128), (0, 0, 0))
# for x in range(160):
#     offset = (x, x)
#     background.paste(image, offset)
#     disp.image(background)

offset = (10, 35)
background.paste(image, offset)
# disp.image(background)
# image = image.crop((10, 40, 110, 90))

drawText = ImageDraw.Draw(background)
# drawText.line((115, 35, 115, 85), fill = (0, 0, 255), width = 5)
# drawText.line((125, 35, 125, 85), fill = (0, 0, 255), width = 4)
# drawText.line((135, 35, 135, 85), fill = (0, 255, 255), width = 3)
# drawText.line((145, 35, 145, 85), fill = (0, 255, 255), width = 2)

drawText.line((115, 40, 115, 80), fill = (0, 0, 255), width = 4)
drawText.line((110, 35, 115, 40), fill = (0, 0, 255), width = 5)
drawText.line((110, 85, 115, 80), fill = (0, 0, 255), width = 5)

px, py = 0.5, 1.0
drawText.text(
    # (0, 0),
    (px*(width - font_width), py*(height - font_height)),
    text,
    font=font,
    fill=(255, 255, 255),
)

disp.image(background)
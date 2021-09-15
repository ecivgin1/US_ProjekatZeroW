import cv2
import numpy as np
from PIL import Image

im_cv = cv2.imread('ETFresizeJPG.jpg')

cv2.imwrite('ETFresizeJPG_cv.jpg', im_cv)

pil_img = Image.fromarray(im_cv)
pil_img.save('ETFresizeJPG_normal.jpg')
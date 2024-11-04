#this python program will fetch an image, and make different 2D FFT analyzes

import numpy as np
from PIL import Image

image = Image.open('IMG_1208.jpg')
print(image.format)
print(image.size)
print(image.mode)

image.show()
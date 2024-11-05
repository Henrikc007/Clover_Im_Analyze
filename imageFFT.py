#this python program will fetch an image, and make different 2D FFT analyzes

import numpy as np
from PIL import Image
import trimmer

mitbillede = trimmer.clovercandidate('IMG_1208.jpg')
print(mitbillede.billede.format)
print(mitbillede.billede.size)
print(mitbillede.billede.mode)


#image.show()
cropimage=mitbillede.klipbillede(2100,1400)
print(cropimage.size)


fadeGreened=cropimage

fadeGreened=trimmer.greenify(fadeGreened,180)
fadeGreened=trimmer.greenify(fadeGreened,180)
fadeGreened=trimmer.greenify(fadeGreened,180)
fadeGreened.show()
cropblackedge=trimmer.createBlackCopy(cropimage)[1]
cropimage.show()




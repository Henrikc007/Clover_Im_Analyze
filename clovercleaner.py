"""A python class that on its own can take an image and clean or add a label if the user finds a clover and/and or multiple clovers where the user can point to the position as well as create a relative size of the clover"""
import numpy as np
from PIL import Image

#the following class interacts with the learningdata\cloves.csv file
class clover_image():
    def __init__(self):
        self.id=0
        self.parent_id=0
        self.bredde=0
        self.hojde=0
        self.type=""
    def getImage(self,image,roleofimage):
        """load the image and depending on role of image it creates a new or several posts in the cloves.csv file, that is setting new areas of clovers leafs etc"""
        if roleofimage=="landscape":
            self.type="landscape"
            
        
if __name__== "__main__":
    myimage=clover_image()
    
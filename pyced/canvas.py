'''
Class representing a canvas to draw

Created on 07.07.2013
@author: Alexey Bright
'''

from math import sqrt
from PIL import Image
from PIL.ImageDraw import ImageDraw

class Canvas(object):
    ' Represents a canvas to draw '

    def __init__(self, width, height, bg = "white"):
        ' Constructs a canvas '
        self.image = Image.new("RGB", (width, height), bg)
        self.drawer = ImageDraw(self.image)
        self.width = width
        self.height = height
        self.color = "black"

    # ----------------------------------------------------------------------- #
    
    def get_image(self):
        ' Returns an image '
        return self.image
        pass
    
    # ----------------------------------------------------------------------- #
    
    def set_color(self, color):
        ' Sets the current color '
        self.color = color
    
    # ----------------------------------------------------------------------- #
    
    def line(self, x1, y1, x2, y2, color = None):
        ' Draws a line from (x1, y1) to (x2, y2) '
        if color is None:
            color = self.color
        self.drawer.line([x1, y1, x2, y2], color)
    
    # ----------------------------------------------------------------------- #
    
    def draw_block(self, instructions):
        ' Draws an image block using drawing instructions '
        pass
    
    # ----------------------------------------------------------------------- #
    
    def show(self):
        self.image.show('Image')
    
    # ----------------------------------------------------------------------- #
    
    def interference(self, src_1, src_2, length):
        sx_1, sy_1 = src_1
        sx_2, sy_2 = src_2
        for x in range(0, self.width):
            x_dist_1 = (x - sx_1) * (x - sx_1)
            x_dist_2 = (x - sx_2) * (x - sx_2)
            for y in range(0, self.height):
                y_dist_1 = (y - sy_1) * (y - sy_1)
                y_dist_2 = (y - sy_2) * (y - sy_2)
                dec_dist_1 = x_dist_1 + y_dist_1
                dec_dist_2 = x_dist_2 + y_dist_2
                mod_1 = sqrt(dec_dist_1) % length
                mod_2 = sqrt(dec_dist_2) % length 
                brt = int(round(255 / length * abs(mod_1 - mod_2)))
                self.image.putpixel((x, y), (brt, 0, 0))

    
    
        
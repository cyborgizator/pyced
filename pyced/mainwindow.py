'''
Class representing the main window to display results

Created on 09.07.2013
@author: Alexey Bright
'''

from PyQt4 import QtGui
from PyQt4 import QtCore

class MainWindow(QtGui.QWidget):
    ' Represents the main window to display results '

    def __init__(self, canvas):
        ' Constructs a window '
        super(MainWindow, self).__init__()
        self.initUI()
        src_image = canvas.get_image()
        dst_image = QtGui.QImage(canvas.width,
                                 canvas.height,
                                 QtGui.QImage.Format_RGB32);
        for x in range(0, canvas.width):
            for y in range(0, canvas.height):
                point = QtCore.QPoint(x, y)
                r, g, b = src_image.getpixel((x, y))
                rgb = (r << 16) | (g << 8) | b
                dst_image.setPixel(point, rgb)
        self.image = dst_image      
    
    # ----------------------------------------------------------------------- #
    
    def initUI(self):
        ' Initializes the UI '
        self.resize(400, 400)
        self.setWindowTitle('PyCED') 
    
    # ----------------------------------------------------------------------- #
        
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        

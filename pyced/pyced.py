'''
Created on 30.04.2013
@author: Alexey Bright
'''

import sys
from PyQt4 import QtGui

from mainwindow import MainWindow
from canvas import Canvas
from structure_source import *
from token import *
from canvas import Canvas

from graph import Graph


def main():
#    app = QtGui.QApplication(sys.argv)
    ss = StructureSource('ph-N=N(+-O)-ph')
#    canvas = Canvas(400, 400, "white")
#    #canvas.interference((161, 198), (199, 235), 7)
#    canvas.line(10, 10, 200, 200, (0, 0, 200))
#    window = MainWindow(canvas)
#    window.show() 
    token = ss.read_radical()
    if token:
        print token.generator

    g1 = Graph({1,2,3})
    g1.connect(1, 2)
    g1.connect(2, 3)
    g1.connect(3, 1)
    g1[4]={1, 2}
    g1.set_trait(4, 'b')
    g1.add_node(5, {2, 3}, 'a')
    for n in g1:
        node, trait = g1[n]
        print(n, " - ", node, trait)

        
#    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    

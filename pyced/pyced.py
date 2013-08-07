'''
Created on 30.04.2013
@author: Alexey Bright
'''

import sys
# from PyQt4 import QtGui

# from mainwindow import MainWindow
#from canvas import Canvas
from structure_source import *
from token import *

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

    g = Graph({1: {2,3}, 2: {3,4}, 3: {4,5}, 4: {5,1}, 5: {1,2}})
    show_graph(g)
    g.set_node(6)
    show_graph(g)
    g.set_node(7, {1,3})
    show_graph(g)
    g.set_node(4, {1})
    show_graph(g)
    
    g.del_node(1)
    show_graph(g)
    g.connect(6,7)
    show_graph(g)
    g.disconnect(3,5)
    show_graph(g)
    print g.get_connected_nodes(3)
    

        
#    sys.exit(app.exec_())

def show_graph(g):
    print '-' * 40
    for n in g:
        node = g[n]
        print(n, " - ", node)
        
        
if __name__ == '__main__':
    main()
    

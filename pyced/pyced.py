'''
Created on 30.04.2013
@author: Alexey Bright
'''

#import sys
# from PyQt4 import QtGui

# from mainwindow import MainWindow
#from canvas import Canvas
#from structure_source import *
#from token import *

from atom import Atom
from mol_graph import MolGraph
from generator import Generator
from locator import Locator
from element import E

def main():
#    app = QtGui.QApplication(sys.argv)
#    ss = StructureSource('ph-N=N(+-O)-ph')
#    canvas = Canvas(400, 400, "white")
#    #canvas.interference((161, 198), (199, 235), 7)
#    canvas.line(10, 10, 200, 200, (0, 0, 200))
#    window = MainWindow(canvas)
#    window.show() 
#    token = ss.read_radical()
#    if token:
#        print token.generator
    
    c1, c2 = Atom(E.C, index = 0), Atom(E.C, index = 1)
    o = Atom(E.O, index = 2)
    mg = MolGraph({c1:{c2}, c2:{c1,o}, o:{c2}})
    g = Generator.create('atom', 'Br')
    Locator([1, 1, 1]).apply_generator(mg, g)
    mg.show()
    print '-' * 80
    g = Generator.create('replace', 'I')
    Locator([5, 6]).apply_generator(mg, g)
    mg.show()
    print '-' * 80
    g = Generator.create('ring', 5)
    Locator([2, 2]).apply_generator(mg, g)
    mg.show()
    print mg.get_brutto_formula()

    
    
    
    
#    sys.exit(app.exec_())
        
        
if __name__ == '__main__':
    main()
    
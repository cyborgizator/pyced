'''
Created on 30.04.2013
@author: Alexey Bright
'''

#import sys
# from PyQt4 import QtGui

# from mainwindow import MainWindow
#from canvas import Canvas
from structure_source import *
#from token import *

from atom import Atom
from mol_graph import MolGraph
from generator import Generator, Chain, Ring, Arene
from modifier import Modifier, Attach, Replace
from locator import Locator
from element import E
from bond import SingleBond

def main():
#    app = QtGui.QApplication(sys.argv)

    ss = StructureSource('H-S-C#N')
    
    # FIX numbering
    
#    canvas = Canvas(400, 400, "white")
#    #canvas.interference((161, 198), (199, 235), 7)
#    canvas.line(10, 10, 200, 200, (0, 0, 200))
#    window = MainWindow(canvas)
#    window.show() 
    radical = ss.read_radical()
    print '=' * 80
    radical.graph.show()
    print 'Current locator:', radical.locator.locants
    
    # -------------------------------------------------------------------------
    
#    mg = Arene(6).build()
#    mg.modify(Locator([1]), Attach(Ring(3)))
#    
#    mg.show()
#
#    print mg.get_brutto_formula()
    
#    sys.exit(app.exec_())
        
        
if __name__ == '__main__':
    main()
    
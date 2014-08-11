__author__ = 'Alexey Bright'

from molecular_graph import MolecularGraph
from atom import Atom
from bond import Bond
from element import Element, E

import xml.etree.ElementTree as eee

def main():
    mg = MolecularGraph()
    a1 = Atom(E.H)
    a2 = Atom(E.Cl)
    b1 = Bond(a1, a2)
    mg.connect(a1, a2, b1)

    print mg.export_to_cml("xyz")



if __name__ == '__main__':
    main()
    
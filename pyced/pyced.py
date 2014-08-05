__author__ = 'Alexey Bright'

from molecular_graph import MolecularGraph

import xml.etree.ElementTree as eee

def main():
    mg = MolecularGraph()
    print mg.export_to_cml("xyz")



if __name__ == '__main__':
    main()
    
__author__ = 'Alexey Bright'

from generators.generator import Generator
from molecular_graph import MolecularGraph
from element import E
from atom import Atom

class AtomGenerator(Generator):

    names = {'Atom'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        element = E.get_element(self.get_argument())
        atom = Atom(element)
        mg.set_atom(1, atom)
        return mg

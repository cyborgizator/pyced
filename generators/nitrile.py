__author__ = 'Alexey Bright'

from generators.generator import FunctionalGroup
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import TripleBond


class Nitrile(FunctionalGroup):

    names = {'CN'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        c_atom = Atom(E.C)
        n_atom = Atom(E.N)
        mg.set_atom(1, c_atom)
        mg.set_atom(2, n_atom)
        mg.add_bond(TripleBond(c_atom, n_atom))
        return mg

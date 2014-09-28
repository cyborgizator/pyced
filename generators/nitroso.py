__author__ = 'Alexey Bright'

from generators.generator import FunctionalGroup
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import DoubleBond


class Nitroso(FunctionalGroup):

    names = {'NO'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        n_atom = Atom(E.N)
        o_atom = Atom(E.O)
        mg.set_atom(1, n_atom)
        mg.set_atom(2, o_atom)
        mg.add_bond(DoubleBond(n_atom, o_atom))
        return mg

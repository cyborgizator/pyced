__author__ = 'Alexey Bright'

from generators.generator import FunctionalGroup
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import DoubleBond


class Isonitrile(FunctionalGroup):

    names = {'NC'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        c_atom = Atom(E.C)
        n_atom = Atom(E.N)
        mg.set_atom(1, n_atom)
        mg.set_atom(2, c_atom)
        mg.add_bond(DoubleBond(n_atom, c_atom))
        return mg

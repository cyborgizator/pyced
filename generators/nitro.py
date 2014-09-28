__author__ = 'Alexey Bright'

from generators.generator import FunctionalGroup
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import DoubleBond


class Nitro(FunctionalGroup):

    names = {'NO2'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        n_atom = Atom(E.N)
        o1_atom = Atom(E.O)
        o2_atom = Atom(E.O)
        mg.set_atom(1, n_atom)
        mg.set_atom(2, o1_atom)
        mg.set_atom(3, o2_atom)
        mg.add_bond(DoubleBond(n_atom, o1_atom))
        mg.add_bond(DoubleBond(n_atom, o2_atom))
        return mg

__author__ = 'Alexey Bright'

from generators.generator import FunctionalGroup
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import SingleBond


class Amine(FunctionalGroup):

    names = {'NH2'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        n_atom = Atom(E.N)
        h1_atom = Atom(E.H)
        h2_atom = Atom(E.H)
        mg.set_atom(1, n_atom)
        mg.set_atom(2, h1_atom)
        mg.set_atom(3, h2_atom)
        mg.add_bond(SingleBond(n_atom, h1_atom))
        mg.add_bond(SingleBond(n_atom, h2_atom))
        return mg

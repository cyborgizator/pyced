__author__ = 'Alexey Bright'

from generators.generator import FunctionalGroup
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import SingleBond, DoubleBond


class Carboxyl(FunctionalGroup):

    names = {'COOH'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        c_atom = Atom(E.C)
        h_atom = Atom(E.C)
        o1_atom = Atom(E.O)
        o2_atom = Atom(E.O)
        mg.set_atom(1, c_atom)
        mg.set_atom(2, o1_atom)
        mg.set_atom(3, o2_atom)
        mg.set_atom(4, h_atom)
        mg.add_bond(DoubleBond(c_atom, o1_atom))
        mg.add_bond(SingleBond(c_atom, o2_atom))
        mg.add_bond(SingleBond(o2_atom, h_atom))
        return mg

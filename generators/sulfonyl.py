__author__ = 'Alexey Bright'

from generators.generator import FunctionalGroup
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import SingleBond, DoubleBond


class Sulfonyl(FunctionalGroup):

    names = {'SO3H'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        s_atom = Atom(E.S)
        h_atom = Atom(E.H)
        o1_atom = Atom(E.O)
        o2_atom = Atom(E.O)
        o3_atom = Atom(E.O)
        mg.set_atom(1, s_atom)
        mg.set_atom(2, o1_atom)
        mg.set_atom(3, o2_atom)
        mg.set_atom(4, o3_atom)
        mg.set_atom(5, h_atom)
        mg.add_bond(DoubleBond(s_atom, o1_atom))
        mg.add_bond(DoubleBond(s_atom, o2_atom))
        mg.add_bond(SingleBond(s_atom, o3_atom))
        mg.add_bond(SingleBond(o3_atom, h_atom))
        return mg

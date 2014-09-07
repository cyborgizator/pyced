__author__ = 'Alexey Bright'

from generators.generator import Generator
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import SingleBond


class Chain(Generator):
    """ Represents an aliphatic chain """

    names = {'C'}

    def build(self):
        """ Returns a generated molecular graph """
        chain = MolecularGraph()
        atom_count = int(self.get_argument())
        prev_atom = Atom(E.C)
        for i in range(1, atom_count):
            atom = Atom(E.C)
            bond = SingleBond(prev_atom, atom)
            chain.add_bond(bond)
            prev_atom = atom
        return chain

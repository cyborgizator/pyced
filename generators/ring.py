__author__ = 'Alexey Bright'

from generators.generator import Generator
from molecular_graph import MolecularGraph
from element import E
from atom import Atom
from bond import SingleBond


class Ring(Generator):

    names = {'O'}

    def build(self):
        """ Returns a generated molecular graph """
        mg = MolecularGraph()
        atom_count = int(self.get_argument())
        prev_atom = Atom(E.C)
        first_atom = prev_atom
        mg.set_atom(1, prev_atom)
        for i in range(1, atom_count):
            atom = Atom(E.C)
            mg.set_atom(i + 1, atom)
            mg.add_bond(SingleBond(prev_atom, atom))
            prev_atom = atom
        mg.add_bond(SingleBond(prev_atom, first_atom))
        return mg

    #TODO rewrite build using chain generator

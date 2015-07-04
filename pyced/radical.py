__author__ = 'Bright'

from locator import Locator
from bond import SingleBond


class Radical:
    """ Represents a radical """

    def __init__(self, mg, locator = None, bond_type = None):
        self.mg = mg
        self.locator = locator if locator else Locator()
        self.bond_type = bond_type if bond_type else SingleBond

    # -------------------------------------------------------------------------
    def attach_radical(self, radical, locator):
        for atom in radical.mg.get_atoms():
            self.mg.add_atom(atom)
        for from_locant in locator:
            from_atom = self.mg.get_atom_by_locant(from_locant)
            for to_locant in radical.locator:
                to_atom = radical.mg.get_atom_by_locant(to_locant)
                bond = radical.bond_type(from_atom, to_atom)
                self.mg.set_bond(bond)

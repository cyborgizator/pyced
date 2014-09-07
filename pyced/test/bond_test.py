__author__ = 'Alexey Bright'

import unittest
from pyced.atom import Atom
from pyced.bond import *
from pyced.element import E


class BondTest(unittest.TestCase):

    def setUp(self):
        self.__a1 = Atom(E.H)
        self.__a2 = Atom(E.Br)
        self.__b1 = Bond.create('-', self.__a1, self.__a2)

    def test_bond(self):
        self.assertEqual(self.__b1.atom1, self.__a1)
        self.assertEqual(self.__b1.atom2, self.__a2)

    def test_get(self):
        self.assertEqual(Bond.get("-"), SingleBond)
        self.assertEqual(Bond.get("+-"), PolarBond)
        self.assertEqual(Bond.get("-+"), ReversedPolarBond)
        self.assertEqual(Bond.get("@@"), Bond)

    def test_create(self):
        atom_c = Atom(E.C)
        atom_o = Atom(E.O)
        bond = Bond.create("=", atom_c, atom_o)
        self.assertIsInstance(bond, DoubleBond)
        self.assertEqual(bond.atom1, atom_c)
        self.assertEqual(bond.atom2, atom_o)


# =============================================================================
if __name__ == "__main__":
    unittest.main()

__author__ = 'Alexey Bright'

import unittest
from pyced.molecular_graph import MolecularGraph
from pyced.atom import Atom
from pyced.bond import Bond
from pyced.element import E


class MolecularGraphTest(unittest.TestCase):

    def setUp(self):
        Atom.reset_id()
        Bond.reset_id()
        self._mg = MolecularGraph()
        self._a1 = Atom(E.H)
        self._a2 = Atom(E.Cl)
        self._b1 = Bond.create("-", self._a1, self._a2)
        self._mg.add_bond(self._b1)

    # -------------------------------------------------------------------------
    def test_get_atoms(self):
        self.assertEquals(self._mg.get_atoms(), {self._a1, self._a2})

    # -------------------------------------------------------------------------
    def test_get_bonds(self):
        self.assertEquals(self._mg.get_bonds(), {self._b1})

    # -------------------------------------------------------------------------
    def test_add_bond(self):
        atom = Atom(E.O)
        bond = Bond.create("=", self._a2, atom)
        self._mg.add_bond(bond)
        self.assertIn(atom, self._mg.get_atoms())
        self.assertIn(bond, self._mg.get_bonds())

    # -------------------------------------------------------------------------
    def test_get_atom_count(self):
        self.assertEqual(self._mg.get_atom_count(), 2)

    # -------------------------------------------------------------------------
    def test_get_atom_by_locant(self):
        self.assertEqual(self._a1, self._mg.get_atom_by_locant(1))
        self.assertEqual(self._a2, self._mg.get_atom_by_locant(2))

    # -------------------------------------------------------------------------
    def test_set_atom(self):
        atom = Atom(E.O)
        self._mg.set_atom(3, atom)
        self.assertEqual(self._mg.get_atom_count(), 3)
        self.assertEqual(self._mg.get_atom_by_locant(3), atom)

    # -------------------------------------------------------------------------
    def test_add_atom(self):
        atom = Atom(E.O)
        self._mg.add_atom(atom)
        self.assertEqual(self._mg.get_atom_count(), 3)
        self.assertEqual(self._mg.get_atom_by_locant(3), atom)

    # -------------------------------------------------------------------------
    def test_replace_atom(self):
        atom = Atom(E.Br)
        self._mg.replace_atom(2, atom)
        self.assertEqual(self._mg.get_atom_count(), 2)
        self.assertEqual(self._mg.get_atom_by_locant(2), atom)

    # -------------------------------------------------------------------------
    def test_get_brutto_formula(self):
        # TODO: make more complex, including C atoms and indices
        self.assertEqual(self._mg.get_brutto_formula(), "HCl")


# =============================================================================
if __name__ == "__main__":
    unittest.main()

__author__ = 'Alexey Bright'

import unittest
from pyced.molecular_graph import MolecularGraph
from pyced.atom import Atom
from pyced.bond import Bond
from pyced.element import E


class MolecularGraphTest(unittest.TestCase):

    def setUp(self):
        self.__mg = MolecularGraph()
        self.__a1 = Atom(E.H)
        self.__a2 = Atom(E.Cl)
        self.__b1 = Bond.create("-", self.__a1, self.__a2)
        self.__mg.add_bond(self.__b1)

    # -------------------------------------------------------------------------
    def test_get_atoms(self):
        self.assertEquals(self.__mg.get_atoms(), {self.__a1, self.__a2})

    # -------------------------------------------------------------------------
    def test_get_bonds(self):
        self.assertEquals(self.__mg.get_bonds(), {self.__b1})

    # -------------------------------------------------------------------------
    def test_add_bond(self):
        atom = Atom(E.O)
        bond = Bond.create("=", self.__a2, atom)
        self.__mg.add_bond(bond)
        self.assertIn(atom, self.__mg.get_atoms())
        self.assertIn(bond, self.__mg.get_bonds())

    # -------------------------------------------------------------------------
    def test_export_to_cml(self):
        hcl = ('<molecule id="HCl"><atomArray>'
               '<atom elementType="H" id="H1" />'
               '<atom elementType="Cl" id="Cl2" /></atomArray>'
               '<bondArray><bond atomRefs2="H1 Cl2" id="H1Cl2" order="S" />'
               '</bondArray></molecule>')
        self.assertEquals(hcl, self.__mg.export_to_cml("HCl"))

# =============================================================================
if __name__ == "__main__":
    unittest.main()

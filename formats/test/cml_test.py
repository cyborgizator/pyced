__author__ = 'Alexey Bright'

import unittest
from pyced.molecular_graph import MolecularGraph
from pyced.atom import Atom
from pyced.bond import Bond
from pyced.element import E
from formats.cml import Cml


class CmlTest(unittest.TestCase):

    def setUp(self):
        Atom.reset_id()
        Bond.reset_id()
        mg = MolecularGraph()
        a1 = Atom(E.H)
        a2 = Atom(E.Cl)
        b = Bond.create("-", a1, a2)
        mg.add_bond(b)
        self._cml = Cml(mg)

    # -------------------------------------------------------------------------
    def test_export(self):
        hcl = ('<molecule id="HCl"><atomArray>'
               '<atom elementType="H" id="H1" />'
               '<atom elementType="Cl" id="Cl2" /></atomArray>'
               '<bondArray><bond atomRefs2="H1 Cl2" id="H1Cl2" order="S" />'
               '</bondArray></molecule>')
        self.assertEquals(hcl, self._cml.export("HCl"))

# =============================================================================
if __name__ == "__main__":
    unittest.main()

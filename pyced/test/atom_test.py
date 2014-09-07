__author__ = 'Alexey Bright'

import unittest
from pyced.atom import Atom
from pyced.element import E


class AtomTest(unittest.TestCase):

    def setUp(self):
        self.__a = Atom(E.C)

    # -------------------------------------------------------------------------
    def test_copy(self):
        copied_atom = self.__a.copy()
        self.assertEqual(self.__a.element, copied_atom.element)
    
    # -------------------------------------------------------------------------
    def test_atom(self):
        self.assertEqual(self.__a.element, E.C)

# =============================================================================
if __name__ == "__main__":
    unittest.main()

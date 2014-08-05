"""
Test case for Atom

Created on 17.05.2014
@author: Bright
"""

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
        self.assertSequenceEqual(self.__a.element, E.C)

# =============================================================================
if __name__ == "__main__":
    import sys;sys.argv = ['', 'AtomTest.test_atom']
    unittest.main()

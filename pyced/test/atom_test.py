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
        self.atom = Atom(E.C,   # element
                         True,  # labelled
                         True,  # ring
                         0,     # index
                         0)     # color

    # -------------------------------------------------------------------------
    def test_calculate_value(self):
        atom_H = Atom(E.H)
        atom_C = Atom(E.C)
        atom_N = Atom(E.N)
        atom_Se = Atom(E.Se)
        self.assertEqual(atom_H.value, 0)
        self.assertEqual(atom_C.value, 1760)
        self.assertEqual(atom_N.value, 384)
        self.assertEqual(atom_Se.value, 245)

    # -------------------------------------------------------------------------
    def test_copy(self):
        copied_atom = self.atom.copy()
        original_props = (self.atom.element,
                          self.atom.labelled,
                          self.atom.ring,
                          self.atom.index,
                          self.atom.value)
        copied_props = (copied_atom.element,
                        copied_atom.labelled,
                        copied_atom.ring,
                        copied_atom.index,
                        copied_atom.value)
        self.assertEqual(original_props, copied_props)
    
    # -------------------------------------------------------------------------
    def test_atom(self):
        atom_props = (self.atom.element,
                      self.atom.labelled,
                      self.atom.ring,
                      self.atom.index)
        self.assertSequenceEqual(atom_props, (E.C, True, True, 0))

# =============================================================================
if __name__ == "__main__":
    import sys;sys.argv = ['', 'AtomTest.test_atom']
    unittest.main()

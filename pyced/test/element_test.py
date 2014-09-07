__author__ = 'Alexey Bright'

import unittest
from pyced.element import E, Element


class ElementTest(unittest.TestCase):

    def setUp(self):
        pass

    # -------------------------------------------------------------------------
    def test_element(self):
        el = Element(300, {-4, 5})
        self.assertEqual(el.atomic_mass, 300)
        self.assertEqual(el.oxidation, {-4, 5})
        self.assertTrue(el.metal)

    def test_get_elements(self):
        self.assertTrue(len(E.get_elements()) > 0)

    def test_get_element(self):
        self.assertTrue(E.get_element("Hg").metal)
        self.assertFalse(E.get_element("S").metal)

    def test_is_element(self):
        self.assertTrue(E.is_element("Ra"))
        self.assertFalse(E.is_element("R"))


# =============================================================================
if __name__ == "__main__":
    unittest.main()

__author__ = 'Alexey Bright'

import unittest
from graphlib.algorithms import ordered_pair


class AlgorithmsTest(unittest.TestCase):

    def setUp(self):
        pass

    # -------------------------------------------------------------------------
    def test_ordered_pair(self):
        self.assertEqual((1, 2), ordered_pair(1, 2))
        self.assertEqual((1, 2), ordered_pair(2, 1))
        self.assertEqual((1, 1), ordered_pair(1, 1))


if __name__ == "__main__":
    unittest.main()
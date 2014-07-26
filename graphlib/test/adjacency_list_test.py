__author__ = 'Alexey Bright'

import unittest
from graphlib.adjacency_list import AdjacencyList
from graphlib.generic_vertex import GenericVertex
from graphlib.exceptions import InvalidLinkError


class AdjacencyListTest(unittest.TestCase):

    def setUp(self):
        self.__al = AdjacencyList()
        self.__v1 = GenericVertex()
        self.__v2 = GenericVertex()
        self.__v3 = GenericVertex()
        self.__v4 = GenericVertex()
        self.__v5 = GenericVertex()
        self.__al.connect(self.__v1, self.__v2)  # 1 -- 2
        self.__al.connect(self.__v1, self.__v3)  # |    |
        self.__al.connect(self.__v2, self.__v4)  # 3 -- 4 -- 5
        self.__al.connect(self.__v4, self.__v5)
        self.__al.connect(self.__v4, self.__v3)

    # -------------------------------------------------------------------------
    def test_init(self):
        self.assertEqual(len(AdjacencyList().get_all_vertices()), 0)

    # -------------------------------------------------------------------------
    def test_connect(self):
        self.__al.connect(self.__v3, self.__v2)
        self.assert_(self.__al.connected(self.__v2, self.__v3))
        self.assertRaises(InvalidLinkError,
                          self.__al.connect,
                          self.__v1,
                          self.__v1)

    # -------------------------------------------------------------------------
    def test_disconnect(self):
        self.__al.disconnect(self.__v1, self.__v2)
        self.assert_(not self.__al.connected(self.__v1, self.__v2))

    # -------------------------------------------------------------------------
    def test_connected(self):
        self.assert_(self.__al.connected(self.__v1, self.__v2))

    # -------------------------------------------------------------------------
    def test_get_connected_vertices(self):
        self.assertEqual(self.__al.get_connected_vertices(self.__v4),
                         {self.__v2, self.__v3, self.__v5})

    # -------------------------------------------------------------------------
    def test_get_all_vertices(self):
        self.assertEqual(self.__al.get_all_vertices(),
                         {self.__v1,
                          self.__v2,
                          self.__v3,
                          self.__v4,
                          self.__v5})


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'AdjacencyListTest.testName']
    unittest.main()
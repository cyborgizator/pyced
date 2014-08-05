__author__ = 'Alexey Bright'

import unittest
from graphlib.generic_link import GenericLink
from graphlib.generic_graph import GenericGraph
from graphlib.generic_vertex import GenericVertex
from graphlib.algorithms import ordered_pair


class GenericGraphTest(unittest.TestCase):

    def setUp(self):
        self.__gg = GenericGraph()
        self.__v1 = GenericVertex()
        self.__v2 = GenericVertex()
        self.__v3 = GenericVertex()
        self.__v4 = GenericVertex()
        self.__v5 = GenericVertex()
        self.__l1 = GenericLink()
        self.__l2 = GenericLink()
        self.__l3 = GenericLink()
        self.__l4 = GenericLink()
        self.__l5 = GenericLink()                            #      1
        self.__gg.connect(self.__v1, self.__v2, self.__l1)   #    1 -- 2
        self.__gg.connect(self.__v1, self.__v3, self.__l2)   # 2  |    | 3
        self.__gg.connect(self.__v2, self.__v4, self.__l3)   #    3 -- 4 -- 5
        self.__gg.connect(self.__v3, self.__v4, self.__l4)   #      4    5
        self.__gg.connect(self.__v4, self.__v5, self.__l5)   #

    # -------------------------------------------------------------------------
    def test_init(self):
        self.assertEqual(len(self.__gg.get_all_links()), 5)
    
    # -------------------------------------------------------------------------
    def test_connect(self):
        link = GenericLink()
        self.__gg.connect(self.__v1, self.__v4, link)
        self.assertEqual(self.__gg.get_link(self.__v1, self.__v4), link)
        self.assert_(self.__gg.connected(self.__v1,self.__v4))

    # -------------------------------------------------------------------------
    def test_disconnect(self):
        self.__gg.disconnect(self.__v1, self.__v2)
        self.assert_(not self.__gg.connected(self.__v1, self.__v2))
    
    # -------------------------------------------------------------------------
    def test_connected(self):
        self.assert_(self.__gg.connected(self.__v1, self.__v2))
        self.assert_(not self.__gg.connected(self.__v1, self.__v4))
    
    # -------------------------------------------------------------------------
    def test_get_link(self):
        self.assertEqual(self.__gg.get_link(self.__v1, self.__v2), self.__l1)
    
    # -------------------------------------------------------------------------
    def test_break_link(self):
        self.__gg.break_link(self.__l1)
        self.assert_(not self.__gg.connected(self.__v1, self.__v2))
    
    # -------------------------------------------------------------------------
    def test_remove_vertex(self):
        self.__gg.remove_vertex(self.__v1)
        self.assert_(not self.__gg.connected(self.__v1, self.__v2))
        self.assert_(not self.__gg.connected(self.__v1, self.__v3))

    def test_get_connected_vertices(self):
        self.assertEqual(self.__gg.get_connected_vertices(self.__v1),
                         {self.__v2, self.__v3})

    # -------------------------------------------------------------------------
    def test_get_linked_vertices(self):
        self.assertEqual(self.__gg.get_linked_vertices(self.__l1),
                         ordered_pair(self.__v1, self.__v2))
    
    # -------------------------------------------------------------------------
    def test_get_adjacent_links(self):
        self.assertEqual({self.__l1, self.__l2},
                         self.__gg.get_adjacent_links(self.__v1))
    
    # -------------------------------------------------------------------------
    def test_get_all_vertices(self):
        self.assertEqual(len(self.__gg.get_all_vertices()), 5)
    
    # -------------------------------------------------------------------------
    def test_get_all_links(self):
        self.assertEqual(len(self.__gg.get_all_links()), 5)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'GenericGraphTest.testName']
    unittest.main()

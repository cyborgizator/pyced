__author__ = 'Alexey Bright'

import unittest
from graphlib.link_list import LinkList
from graphlib.generic_vertex import GenericVertex
from graphlib.generic_link import GenericLink
from graphlib.algorithms import ordered_pair


class LinkListTest(unittest.TestCase):

    def setUp(self):
        self.__ll = LinkList()
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
        self.__ll.connect(self.__v1, self.__v2, self.__l1)   #    1 -- 2
        self.__ll.connect(self.__v1, self.__v3, self.__l2)   # 2  |    | 3
        self.__ll.connect(self.__v2, self.__v4, self.__l3)   #    3 -- 4 -- 5
        self.__ll.connect(self.__v3, self.__v4, self.__l4)   #      4    5
        self.__ll.connect(self.__v4, self.__v5, self.__l5)   #

    # -------------------------------------------------------------------------
    def test_connect(self):
        link = GenericLink()
        self.__ll.connect(self.__v1, self.__v2, link)
        self.assertEqual(self.__ll.get_linked_vertices(link),
                         ordered_pair(self.__v1, self.__v2))
    
    # -------------------------------------------------------------------------
    def test_break_link(self):
        self.__ll.break_link(self.__l1)
        vertex_pairs = self.__ll.get_all_connected_vertices()
        self.assert_(not ordered_pair(self.__v1, self.__v2) in vertex_pairs)
    
    # -------------------------------------------------------------------------
    def test_get_linked_vertices(self):
        vertex_pair = self.__ll.get_linked_vertices(self.__l1)
        self.assertEqual(ordered_pair(self.__v1, self.__v2), vertex_pair)
    
    # -------------------------------------------------------------------------
    def test_get_all_connected_vertices(self):
        vertex_pairs = self.__ll.get_all_connected_vertices()
        self.assertEqual(len(vertex_pairs), 5)
    
    # -------------------------------------------------------------------------
    def test_get_all_links(self):
        links = self.__ll.get_all_links()
        self.assertEqual(len(links), 5)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'LinkListTest.testName']
    unittest.main()

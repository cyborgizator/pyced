__author__ = 'Alexey Bright'

import unittest
from graphlib.generic_link import GenericLink
from graphlib.generic_graph import GenericGraph
from graphlib.generic_vertex import GenericVertex
from graphlib.algorithms import ordered_pair


class GenericGraphTest(unittest.TestCase):

    def setUp(self):
        self._gg = GenericGraph()
        self._v1 = GenericVertex()
        self._v2 = GenericVertex()
        self._v3 = GenericVertex()
        self._v4 = GenericVertex()
        self._v5 = GenericVertex()
        self._l1 = GenericLink()
        self._l2 = GenericLink()
        self._l3 = GenericLink()
        self._l4 = GenericLink()
        self._l5 = GenericLink()                         #      1
        self._gg.connect(self._v1, self._v2, self._l1)   #    1 -- 2
        self._gg.connect(self._v1, self._v3, self._l2)   # 2  |    | 3
        self._gg.connect(self._v2, self._v4, self._l3)   #    3 -- 4 -- 5
        self._gg.connect(self._v3, self._v4, self._l4)   #      4    5
        self._gg.connect(self._v4, self._v5, self._l5)   #

    # -------------------------------------------------------------------------
    def test_init(self):
        self.assertEqual(len(self._gg.get_all_links()), 5)

    # -------------------------------------------------------------------------
    def test_add_vertex(self):
        v = GenericVertex()
        self._gg.add_vertex(v)
        self.assertEqual(self._gg.get_connected_vertices(v), set())

    # -------------------------------------------------------------------------
    def test_connect(self):
        link = GenericLink()
        self._gg.connect(self._v1, self._v4, link)
        self.assertEqual(self._gg.get_link(self._v1, self._v4), link)
        self.assert_(self._gg.connected(self._v1, self._v4))

    # -------------------------------------------------------------------------
    def test_disconnect(self):
        self._gg.disconnect(self._v1, self._v2)
        self.assert_(not self._gg.connected(self._v1, self._v2))

    # -------------------------------------------------------------------------
    def test_connected(self):
        self.assert_(self._gg.connected(self._v1, self._v2))
        self.assert_(not self._gg.connected(self._v1, self._v4))

    # -------------------------------------------------------------------------
    def test_get_link(self):
        self.assertEqual(self._gg.get_link(self._v1, self._v2), self._l1)

    # -------------------------------------------------------------------------
    def test_break_link(self):
        self._gg.break_link(self._l1)
        self.assert_(not self._gg.connected(self._v1, self._v2))

    # -------------------------------------------------------------------------
    def test_remove_vertex(self):
        self._gg.remove_vertex(self._v1)
        self.assert_(not self._gg.connected(self._v1, self._v2))
        self.assert_(not self._gg.connected(self._v1, self._v3))

    def test_get_connected_vertices(self):
        self.assertEqual(self._gg.get_connected_vertices(self._v1),
                         {self._v2, self._v3})

    # -------------------------------------------------------------------------
    def test_get_linked_vertices(self):
        self.assertEqual(self._gg.get_linked_vertices(self._l1),
                         ordered_pair(self._v1, self._v2))

    # -------------------------------------------------------------------------
    def test_get_adjacent_links(self):
        self.assertEqual({self._l1, self._l2},
                         self._gg.get_adjacent_links(self._v1))

    # -------------------------------------------------------------------------
    def test_get_all_vertices(self):
        self.assertEqual(len(self._gg.get_all_vertices()), 5)

    # -------------------------------------------------------------------------
    def test_get_all_links(self):
        self.assertEqual(len(self._gg.get_all_links()), 5)

    # -------------------------------------------------------------------------
    def test_replace_node(self):
        v = GenericVertex()
        self._gg.replace_node(self._v4, v)
        self.assertEqual({self._v2, self._v3, self._v5},
                         self._gg.get_connected_vertices(v))
        self.assertEqual({self._l3, self._l4, self._l5},
                         self._gg.get_adjacent_links(v))
        self.assertEqual(self._gg.get_connected_vertices(self._v5), {v})


if __name__ == "__main__":
    unittest.main()

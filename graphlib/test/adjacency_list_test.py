__author__ = 'Alexey Bright'

import unittest
from graphlib.adjacency_list import AdjacencyList
from graphlib.generic_vertex import GenericVertex
from graphlib.exceptions import InvalidLinkError


class AdjacencyListTest(unittest.TestCase):

    def setUp(self):
        self._al = AdjacencyList()
        self._v1 = GenericVertex()
        self._v2 = GenericVertex()
        self._v3 = GenericVertex()
        self._v4 = GenericVertex()
        self._v5 = GenericVertex()
        self._al.connect(self._v1, self._v2)  # 1 -- 2
        self._al.connect(self._v1, self._v3)  # |    |
        self._al.connect(self._v2, self._v4)  # 3 -- 4 -- 5
        self._al.connect(self._v4, self._v5)
        self._al.connect(self._v4, self._v3)

    # -------------------------------------------------------------------------
    def test_init(self):
        self.assertEqual(len(AdjacencyList().get_all_vertices()), 0)

    # -------------------------------------------------------------------------
    def test_add_vertex(self):
        v = GenericVertex()
        self._al.add_vertex(v)
        self.assertEqual(self._al.get_connected_vertices(v), set())

    # -------------------------------------------------------------------------
    def test_connect(self):
        self._al.connect(self._v3, self._v2)
        self.assert_(self._al.connected(self._v2, self._v3))
        self.assertRaises(InvalidLinkError,
                          self._al.connect,
                          self._v1,
                          self._v1)

    # -------------------------------------------------------------------------
    def test_disconnect(self):
        self._al.disconnect(self._v1, self._v2)
        self.assert_(not self._al.connected(self._v1, self._v2))

    # -------------------------------------------------------------------------
    def test_connected(self):
        self.assert_(self._al.connected(self._v1, self._v2))

    # -------------------------------------------------------------------------
    def test_get_connected_vertices(self):
        self.assertEqual(self._al.get_connected_vertices(self._v4),
                         {self._v2, self._v3, self._v5})

    # -------------------------------------------------------------------------
    def test_get_all_vertices(self):
        self.assertEqual(self._al.get_all_vertices(),
                         {self._v1,
                          self._v2,
                          self._v3,
                          self._v4,
                          self._v5})

    # -------------------------------------------------------------------------
    def test_remove_vertex(self):
        self._al.remove_vertex(self._v3)
        self.assertNotIn(self._v3, self._al.get_all_vertices())
        self.assertNotIn(self._v3, self._al.get_connected_vertices(self._v1))
        self.assertNotIn(self._v3, self._al.get_connected_vertices(self._v4))

    # -------------------------------------------------------------------------
    def test_replace_vertex(self):
        new_v = GenericVertex()
        self._al.replace_vertex(self._v3, new_v)
        self.assertNotIn(self._v3, self._al.get_all_vertices())
        self.assertNotIn(self._v3, self._al.get_connected_vertices(self._v1))
        self.assertNotIn(self._v3, self._al.get_connected_vertices(self._v4))
        self.assert_(self._al.connected(new_v, self._v1))
        self.assert_(self._al.connected(new_v, self._v4))


if __name__ == "__main__":
    unittest.main()

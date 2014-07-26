__author__ = 'Alexey Bright'

import unittest
from graphlib.connect_list import ConnectList
from graphlib.generic_vertex import GenericVertex
from graphlib.generic_link import GenericLink


class ConnectListTest(unittest.TestCase):

    def setUp(self):
        self.__cl = ConnectList()
        self.__v1 = GenericVertex()
        self.__v2 = GenericVertex()
        self.__v3 = GenericVertex()
        self.__v4 = GenericVertex()
        self.__v5 = GenericVertex()
        self.__l1 = GenericLink()
        self.__l2 = GenericLink()
        self.__l3 = GenericLink()
        self.__l4 = GenericLink()
        self.__l5 = GenericLink()                           #      1
        self.__cl.connect(self.__v1, self.__v2, self.__l1)  #    1 -- 2
        self.__cl.connect(self.__v1, self.__v3, self.__l2)  # 2  |    | 3
        self.__cl.connect(self.__v2, self.__v4, self.__l3)  #    3 -- 4 -- 5
        self.__cl.connect(self.__v3, self.__v4, self.__l4)  #      4    5
        self.__cl.connect(self.__v4, self.__v5, self.__l5)

    # -------------------------------------------------------------------------
    def test_connect(self):
        link = GenericLink()
        self.__cl.connect(self.__v1, self.__v4, link)
        self.assertEqual(self.__cl.get_link(self.__v1, self.__v4), link)

    # -------------------------------------------------------------------------
    def test_disconnect(self):
        self.__cl.disconnect(self.__v1, self.__v2)
        self.assert_(not self.__cl.connected(self.__v1, self.__v2))

    # -------------------------------------------------------------------------
    def test_connected(self):
        self.assert_(self.__cl.connected(self.__v4, self.__v5))

    # -------------------------------------------------------------------------
    def test_get_link(self):
        link = self.__cl.get_link(self.__v1, self.__v2)
        self.assertEqual(link, self.__l1)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'ConnectListTest.testName']
    unittest.main()
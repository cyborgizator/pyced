__author__ = 'Alexey Bright'

import unittest
from graphlib.generic_link import GenericLink


class GenericLinkTest(unittest.TestCase):

    def setUp(self):
        GenericLink.reset_id()
        self.__l1 = GenericLink()
        self.__l2 = GenericLink()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
__author__ = 'Alexey Bright'

import unittest
from graphlib.generic_vertex import GenericVertex


class GenericVertexTest(unittest.TestCase):

    def setUp(self):
        GenericVertex.reset_id()
        self.__v1 = GenericVertex()
        self.__v2 = GenericVertex()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'GenericVertexTest.testName']
    unittest.main()
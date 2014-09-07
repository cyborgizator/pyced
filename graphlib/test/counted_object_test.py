__author__ = 'Alexey Bright'

import unittest
from graphlib.counted_object import CountedObject


class Test(unittest.TestCase):

    def setUp(self):
        CountedObject.reset_id()
        self.__o1 = CountedObject()
        self.__o2 = CountedObject()

    # -------------------------------------------------------------------------
    def test_init(self):
        self.assertLess(self.__o1.get_id(), self.__o2.get_id())
    
    # -------------------------------------------------------------------------
    def test_lt(self):
        self.assertLess(self.__o1, self.__o2)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Alexey Bright'

from graphlib.generic_vertex import GenericVertex
from element import E


class Atom(GenericVertex):
    """ Represents a single atom """

    # -------------------------------------------------------------------------
    def __init__(self, element):
        """ Creates Atom object of given element """
        super(self.__class__, self).__init__()
        self.__element = element

    # -------------------------------------------------------------------------
    def copy(self):
        """ Returns copy of the atom """
        return Atom(self.__element)

    # -------------------------------------------------------------------------
    def calculate_value(self):
        """ Calculates and returns comparison value of the atom """
        value = 0
        if self.__element != E.H:
            value = (1 << 10) if self.__element == E.C else 0
            value |= (ord('Z') - ord(self.__element.symbol[0])) << 5
            if len(self.__element.symbol) > 1:
                value |= ord('z') - ord(self.__element.symbol[1])
        return value
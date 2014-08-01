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

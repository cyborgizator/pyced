__author__ = 'Alexey Bright'

from bond import Bond
#from generator import Generator
#from modifier import Modifier


class IcedToken(object):
    """ Represents a single token of the ICED syntax """
    pass


# =============================================================================
class NumberToken(IcedToken):
    """ Represents a number token """

    def __init__(self, number):
        self.__number = int(number)

    # -------------------------------------------------------------------------
    def build(self):
        return self.__number


# =============================================================================
class BondToken(IcedToken):
    """ Represent a bond token """

    def __init__(self, symbol):
        self.__symbol = symbol

    # -------------------------------------------------------------------------
    def build(self, atom1, atom2):
        return Bond.create(self.__symbol, atom1, atom2)

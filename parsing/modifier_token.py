__author__ = 'Alexey Bright'

from parsing.locator_token import IcedToken


class ModifierToken(IcedToken):
    """ Represents a modifier token """

    def __init__(self, name, arg = None):
        self.__name = name
        self.__arg = arg

    # -------------------------------------------------------------------------
    def build(self):
        #TODO build modifier by token
        pass

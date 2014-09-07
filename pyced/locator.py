__author__ = 'Alexey Bright'


class Locator(object):
    """ Represents a locator """

    def __init__(self, locants = None):
        if locants:
            self.__locants = locants
        else:
            self.__locants = []

    # -------------------------------------------------------------------------
    def add_locant(self, locant):
        self.__locants.append(locant)

    # -------------------------------------------------------------------------
    def add_locants(self, locants):
        self.__locants += locants

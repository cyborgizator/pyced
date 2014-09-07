__author__ = 'Alexey Bright'

from parsing.iced_token import IcedToken
from pyced.locator import Locator


class LocatorToken(IcedToken):
    """ Represents a locator token """

    def __init__(self, number):
        self.__locants = [number]
        #TODO replace create methods by recursive constructor

    # -------------------------------------------------------------------------
    def add_locant(self, number):
        self.__locants.append(number)

    # -------------------------------------------------------------------------
    def build(self):
        #TODO build locator by token
        pass

    # -------------------------------------------------------------------------
    @staticmethod
    def create_from_n(number):
        return LocatorToken(number)

    # -------------------------------------------------------------------------
    @staticmethod
    def create_from_ln(locator, number):
        locator.add_locant(number)
        return locator

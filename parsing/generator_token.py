__author__ = 'Alexey Bright'

from parsing.iced_token import IcedToken


class GeneratorToken(IcedToken):
    """ Represents a generator token """

    def build(self):
        # empty builder
        pass


# =============================================================================
# Id and Id[n] variants
class IdGeneratorToken(GeneratorToken):

    def __init__(self, name, arg):
        self.__name = name
        self.__arg = arg

    # -------------------------------------------------------------------------
    def build(self):
        #TODO build generator by token
        #return Generator(self.__name, self.__arg)
        pass


# =============================================================================
# E variant
class EGeneratorToken(GeneratorToken):

    def __init__(self, element):
        self.__element = element

    # -------------------------------------------------------------------------
    def build(self):
        #TODO build generator by token
        pass


# =============================================================================
# M variant
class MGeneratorToken(GeneratorToken):

    def __init__(self, modifier):
        self.__modifier = modifier

    # -------------------------------------------------------------------------
    def build(self):
        #TODO build generator by token
        pass

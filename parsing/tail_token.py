__author__ = 'Alexey Bright'

from parsing.iced_token import IcedToken


# Tail expression   T ::= LT | MT | BRT | e
class TailToken(IcedToken):
    """ Represents a tail token """

    def __init__(self, tail):
        self.__tail = tail

    # -------------------------------------------------------------------------
    def apply_to(self, radical):
        # empty applicator
        pass


# =============================================================================
# LT variant
class LtTailToken(TailToken):

    def __init__(self, locator, tail = None):
        super(self.__class__, self).__init__(tail)
        self.__locator = locator

    # -------------------------------------------------------------------------
    def apply_to(self, radical):
        radical.set_locator(self.__locator)
        self.__tail.apply_to(radical)


# =============================================================================
# MT variant
class MtTailToken(TailToken):

    def __init__(self, modifier, tail = None):
        super(self.__class__, self).__init__(tail)
        self.__modifier = modifier

    # -------------------------------------------------------------------------
    def apply_to(self, radical):
        radical.modify(self.__modifier)
        self.__tail.apply_to(radical)


# =============================================================================
# BRT variant
class BrtTailToken(TailToken):

    def __init__(self, bond, radical, tail = None):
        super(self.__class__, self).__init__(tail)
        self.__bond = bond
        self.__radical = radical

    # -------------------------------------------------------------------------
    def apply_to(self, radical):
        radical.attach(self.__radical, self.__bond)
        self.__tail.apply_to(radical)


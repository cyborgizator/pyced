__author__ = 'Alexey Bright'

from parsing.iced_token import IcedToken


# Radical       R ::= (R)T | GT
class RadicalToken(IcedToken):
    """ Represents a radical token """

    def __init__(self, tail):
        self.__tail = tail

    # -------------------------------------------------------------------------
    def build(self):
        # empty builder
        return None


# =============================================================================
# (R)T variant
class RtRadicalToken(RadicalToken):

    def __init__(self, radical, tail = None):
        super(self.__class__, self).__init__(tail)
        self.__radical = radical

    # -------------------------------------------------------------------------
    def build(self):
        radical = self.__radical.build()
        self.__tail.apply_to(radical)
        return radical


# =============================================================================
# GT variant
class GtRadicalToken(RadicalToken):

    def __init__(self, generator, tail = None):
        super(self.__class__, self).__init__(tail)
        self.__generator = generator

    # -------------------------------------------------------------------------
    def build(self):
        radical = self.__generator.generate()
        self.__tail.apply_to(radical)
        return radical

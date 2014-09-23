__author__ = 'Alexey Bright'

from generators.generator_factory import MetaGenerator


class Generator(object):
    """ Represents a generator """
    __metaclass__ = MetaGenerator

    def __init__(self, arg):
        self.__arg = arg

    # -------------------------------------------------------------------------
    def get_argument(self):
        return self.__arg


# =============================================================================
class FunctionalGroup(Generator):
    pass


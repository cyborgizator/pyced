__author__ = 'Alexey Bright'

from modifiers.modifier_factory import MetaModifier


class Modifier(object):
    """ Represents a modifier """
    __metaclass__ = MetaModifier

    def __init__(self, **args):
        self._args = args

    # -------------------------------------------------------------------------
    def get_argument(self):
        return self._args

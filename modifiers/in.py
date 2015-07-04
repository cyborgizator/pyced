__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class In(Modifier):
    """ Represents triple bond """

    names = {'in'}

    def apply(self):
        """ Applies modifier to the molecular graph """
        pass

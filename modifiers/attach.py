__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class Attach(Modifier):
    """ Represents attachment of a radical """

    names = {'attach'}

    def apply(self):
        """ Applies modifier to the molecular graph """
        pass

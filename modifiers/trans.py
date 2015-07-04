__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class Trans(Modifier):
    """ Represents trans-bond """

    names = {'trans'}

    def apply(self):
        """ Applies modifier to the molecular graph """
        pass

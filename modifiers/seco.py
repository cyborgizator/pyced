__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class Seco(Modifier):
    """ Represents removing of the bond """

    names = {'seco'}

    def apply(self):
        """ Applies modifier to the molecular graph """
        pass

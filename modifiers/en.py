__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class En(Modifier):
    """ Represents double bond """

    names = {'en'}

    def apply(self):
        """ Applies modifier to the molecular graph """
        pass

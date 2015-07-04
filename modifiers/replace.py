__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class Replace(Modifier):
    """ Represents replacement of an atom """

    names = {'replace'}

    def apply(self):
        """ Applies modifier to the molecular graph """
        pass

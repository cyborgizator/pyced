__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class Cis(Modifier):
    """ Represents cis-bond """

    names = {'cis'}

    def apply(self):
        """ Applies modifier to the molecular graph """
        pass

__author__ = 'Alexey Bright'

from modifiers.modifier import Modifier


class Attach(Modifier):
    """ Represents attachment of a radical
        Arguments:
            radical - radical to be attached
            locator - placement of the radical
    """

    names = {'attach'}

    def apply(self, mg):
        """ Applies modifier to the molecular graph
            @:arg mg is a molecular graph to be modified
        """
        assert 'radical' in self._args
        assert 'locator' in self._args

        # TODO: implement it

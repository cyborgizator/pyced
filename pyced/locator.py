__author__ = 'Alexey Bright'


class Locator(object):
    """ Represents a locator """

    def __init__(self, locants = None):
        """ Constructs a locator
            :param locants: list of locants
        """
        if locants:
            self._locants = locants
        else:
            self._locants = []

    # -------------------------------------------------------------------------
    def add_locant(self, locant):
        """ Appends a new locant to the list
            :param locant: a locant to be appended
        """
        self._locants.append(locant)

    # -------------------------------------------------------------------------
    def add_locants(self, locants):
        """ Append locants to the list
            :param locants: locants to be appended
        """
        self._locants += locants

    # -------------------------------------------------------------------------
    def get_first(self):
        """ Returns the first of the locants """
        return self._locants[0] if len(self._locants) else 0

    # Sequence interface
    # -------------------------------------------------------------------------
    def __len__(self):
        return len(self._locants)

    # -------------------------------------------------------------------------
    def __getitem__(self, index):
        return self._locants[index]

    # -------------------------------------------------------------------------
    def __iter__(self):
        return iter(self._locants)

    # -------------------------------------------------------------------------
    def __contains__(self, locant):
        return locant in self._locants

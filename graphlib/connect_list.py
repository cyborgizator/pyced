__author__ = 'Alexey Bright'

from collections import OrderedDict
from algorithms import ordered_pair


class ConnectList(object):
    """ Graph representation as an connection list """

    # -------------------------------------------------------------------------
    def __init__(self):
        self._items = OrderedDict()

    # -------------------------------------------------------------------------
    def connect(self, v1, v2, link):
        """ Connects v1 and v2 vertices with link """
        self._items[ordered_pair(v1, v2)] = link

    # -------------------------------------------------------------------------
    def disconnect(self, v1, v2):
        """ Breaks link between v1 and v2 """
        assert ordered_pair(v1, v2) in self._items, \
            "Vertices aren't connected"
        self._items.pop(ordered_pair(v1, v2))

    # -------------------------------------------------------------------------
    def connected(self, v1, v2):
        """ Checks if v1 and v2 are connected """
        return ordered_pair(v1, v2) in self._items

    # -------------------------------------------------------------------------
    def get_link(self, v1, v2):
        """ Returns links by given vertices """
        assert ordered_pair(v1, v2) in self._items, \
            "Vertices aren't connected"
        return self._items[ordered_pair(v1, v2)]


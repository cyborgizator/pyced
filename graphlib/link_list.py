__author__ = 'Alexey Bright'


class LinkList(object):
    """ Graph representation as an links list """

    # -------------------------------------------------------------------------
    def __init__(self):
        self._items = {}

    # -------------------------------------------------------------------------
    def connect(self, v1, v2, link):
        """ Connects v1 and v2 vertices with link """
        self._items[link] = (v1, v2)

    # -------------------------------------------------------------------------
    def break_link(self, link):
        """ Breaks link """
        assert link in self._items, "Link doesn't exist"
        del self._items[link]

    # -------------------------------------------------------------------------
    def get_linked_vertices(self, link):
        """ Returns tuple of vertices for given link """
        assert link in self._items, "Link doesn't exist"
        return self._items[link]

    # -------------------------------------------------------------------------
    def get_all_connected_vertices(self):
        """ Returns all the tuples of the vertices as a list """
        return self._items.values()

    # -------------------------------------------------------------------------
    def get_all_links(self):
        """ Returns set of all the links """
        return set(self._items.keys())

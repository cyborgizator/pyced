__author__ = 'Alexey Bright'

from exceptions import InvalidLinkError


class AdjacencyList(object):
    """ Graph representation as an adjacency list """

    def __init__(self):
        self.__items = {}

    # -------------------------------------------------------------------------
    def add_vertex(self, v):
        """ Adds a new vertex to the graph """
        self.__items[v] = {}

    # -------------------------------------------------------------------------
    def connect(self, v1, v2):
        """ Connects v1 and v2 vertices """
        if v1 == v2:
            raise InvalidLinkError("Trying to connect vertex to itself")
        if v1 in self.__items:
            self.__items[v1].add(v2)
        else:
            self.__items[v1] = {v2}
        if v2 in self.__items:
            self.__items[v2].add(v1)
        else:
            self.__items[v2] = {v1}

    # -------------------------------------------------------------------------
    def disconnect(self, v1, v2):
        """ Break link between v1 and v2 vertices """
        assert (v2 in self.__items[v1]) & (v1 in self.__items[v2]), \
            "Vertices aren't connected"
        self.__items[v1].discard(v2)
        self.__items[v2].discard(v1)

    # -------------------------------------------------------------------------
    def connected(self, v1, v2):
        """ Checks if v1 and v2 vertices are connected """
        return v2 in self.__items[v1]

    # -------------------------------------------------------------------------
    def get_connected_vertices(self, v):
        """ Returns set of connected vertices by given vertex """
        assert v in self.__items, "Vertex doesn't exist"
        return self.__items[v]

    # -------------------------------------------------------------------------
    def get_all_vertices(self):
        """ Return set of all the vertices """
        return set(self.__items.keys())


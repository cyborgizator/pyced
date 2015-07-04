__author__ = 'Alexey Bright'

from exceptions import InvalidLinkError


class AdjacencyList(object):
    """ Graph representation as an adjacency list """

    def __init__(self):
        self._items = {}

    # -------------------------------------------------------------------------
    def get_vertex_count(self):
        """ Returns number of the vertices """
        return len(self._items)

    # -------------------------------------------------------------------------
    def add_vertex(self, v):
        """ Adds a new vertex to the graph """
        self._items[v] = set()

    # -------------------------------------------------------------------------
    def connect(self, v1, v2):
        """ Connects v1 and v2 vertices """
        if v1 == v2:
            raise InvalidLinkError("Trying to connect vertex to itself")
        if v1 in self._items:
            self._items[v1].add(v2)
        else:
            self._items[v1] = {v2}
        if v2 in self._items:
            self._items[v2].add(v1)
        else:
            self._items[v2] = {v1}

    # -------------------------------------------------------------------------
    def disconnect(self, v1, v2):
        """ Break link between v1 and v2 vertices """
        self._items[v1].discard(v2)
        self._items[v2].discard(v1)

    # -------------------------------------------------------------------------
    def connected(self, v1, v2):
        """ Checks if v1 and v2 vertices are connected """
        return v2 in self._items[v1]

    # -------------------------------------------------------------------------
    def get_connected_vertices(self, v):
        """ Returns set of connected vertices by given vertex """
        return self._items[v]

    # -------------------------------------------------------------------------
    def get_all_vertices(self):
        """ Return set of all the vertices """
        return set(self._items.keys())

    # -------------------------------------------------------------------------
    def remove_vertex(self, v):
        """ Removes vertex and break all the adjacent edges
        :param v: vertex to be removed """
        vertices = self.get_connected_vertices(v)
        del self._items[v]
        for vertex in vertices:
            self._items[vertex].discard(v)

    # -------------------------------------------------------------------------
    def replace_vertex(self, old_v, new_v):
        """ Replaces vertex
        :param old_v: vertex to be replaced
        :param new_v: replacing vertex """
        vertices = self.get_connected_vertices(old_v)
        self._items[new_v] = vertices
        del self._items[old_v]
        for vertex in vertices:
            self._items[vertex].discard(old_v)
            self._items[vertex].add(new_v)

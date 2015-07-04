__author__ = 'Alexey Bright'

import adjacency_list
import connect_list
import link_list


class GenericGraph(object):
    """ Represents a generic graph """

    # -------------------------------------------------------------------------
    def __init__(self):
        self._adjacency_list = adjacency_list.AdjacencyList()
        self._connect_list = connect_list.ConnectList()
        self._link_list = link_list.LinkList()

    # -------------------------------------------------------------------------
    def get_vertex_count(self):
        """ Returns number of the vertices """
        return self._adjacency_list.get_vertex_count()

    # -------------------------------------------------------------------------
    def add_vertex(self, v):
        """ Adds a new vertex to the graph """
        self._adjacency_list.add_vertex(v)

    # -------------------------------------------------------------------------
    def connect(self, v1, v2, link):
        """ Connects v1 and v2 vertices with link """
        if self.connected(v1, v2):
            self.disconnect(v1, v2)
        self._adjacency_list.connect(v1, v2)
        self._connect_list.connect(v1, v2, link)
        self._link_list.connect(v1, v2, link)

    # -------------------------------------------------------------------------
    def disconnect(self, v1, v2):
        """ Disconnects v1 and v2 vertices """
        self._adjacency_list.disconnect(v1, v2)
        link = self._connect_list.get_link(v1, v2)
        self._connect_list.disconnect(v1, v2)
        self._link_list.break_link(link)

    # -------------------------------------------------------------------------
    def connected(self, v1, v2):
        """ Checks if v1 and v2 vertices are connected """
        return self._connect_list.connected(v1, v2)

    # -------------------------------------------------------------------------
    def get_link(self, v1, v2):
        """ Returns link connecting given vertices """
        return self._connect_list.get_link(v1, v2)

    # -------------------------------------------------------------------------
    def break_link(self, link):
        """ Breaks given link """
        (v1, v2) = self._link_list.get_linked_vertices(link)
        self._link_list.break_link(link)
        self._connect_list.disconnect(v1, v2)
        self._adjacency_list.disconnect(v1, v2)

    # -------------------------------------------------------------------------
    def remove_vertex(self, v):
        """ Removes given vertex from the graph """
        connected_vertices = self._adjacency_list.get_connected_vertices(v)
        for connected_vertex in list(connected_vertices):
            adjacent_link = self._connect_list.get_link(v, connected_vertex)
            self._connect_list.disconnect(v, connected_vertex)
            self._adjacency_list.disconnect(v, connected_vertex)
            self._link_list.break_link(adjacent_link)

    # -------------------------------------------------------------------------
    def get_connected_vertices(self, v):
        """ Returns set of vertices adjacent to the given one """
        return self._adjacency_list.get_connected_vertices(v)

    # -------------------------------------------------------------------------
    def get_linked_vertices(self, link):
        """ Returns tuple of vertices for given link """
        return self._link_list.get_linked_vertices(link)

    # -------------------------------------------------------------------------
    def get_adjacent_links(self, v):
        """ Returns adjacent links for given vertex """
        adjs = self._adjacency_list.get_connected_vertices(v)
        links = [self._connect_list.get_link(v, vertex) for vertex in adjs]
        return set(links)

    # -------------------------------------------------------------------------
    def get_all_vertices(self):
        """ Returns all the vertices in the graph """
        return self._adjacency_list.get_all_vertices()

    # -------------------------------------------------------------------------
    def get_all_links(self):
        """ Returns all the links in the graph """
        return self._link_list.get_all_links()

    # -------------------------------------------------------------------------
    def replace_node(self, old_v, new_v):
        """ Replace vertex with the new one
        :param old_v: vertex to be replaced
        :param new_v: replacing vertex """
        vertices = self._adjacency_list.get_connected_vertices(old_v)
        self._adjacency_list.replace_vertex(old_v, new_v)
        for v in vertices:
            link = self._connect_list.get_link(old_v, v)
            self._connect_list.disconnect(old_v, v)
            self._connect_list.connect(new_v, v, link)
            self._link_list.break_link(link)
            self._link_list.connect(new_v, v, link)


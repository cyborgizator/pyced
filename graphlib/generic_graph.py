__author__ = 'Alexey Bright'

import adjacency_list
import connect_list
import link_list


class GenericGraph(object):
    """ Represents a generic graph """

    # -------------------------------------------------------------------------
    def __init__(self):
        self.__adjacency_list = adjacency_list.AdjacencyList()
        self.__connect_list = connect_list.ConnectList()
        self.__link_list = link_list.LinkList()

    # -------------------------------------------------------------------------
    def add_vertex(self, v):
        """ Adds a new vertex to the graph """
        self.__adjacency_list.add_vertex(v)

    # -------------------------------------------------------------------------
    def connect(self, v1, v2, link):
        """ Connects v1 and v2 vertices with link """
        if self.connected(v1, v2):
            self.disconnect(v1, v2)
        self.__adjacency_list.connect(v1, v2)
        self.__connect_list.connect(v1, v2, link)
        self.__link_list.connect(v1, v2, link)

    # -------------------------------------------------------------------------
    def disconnect(self, v1, v2):
        """ Disconnects v1 and v2 vertices """
        self.__adjacency_list.disconnect(v1, v2)
        link = self.__connect_list.get_link(v1, v2)
        self.__connect_list.disconnect(v1, v2)
        self.__link_list.break_link(link)

    # -------------------------------------------------------------------------
    def connected(self, v1, v2):
        """ Checks if v1 and v2 vertices are connected """
        return self.__connect_list.connected(v1, v2)

    # -------------------------------------------------------------------------
    def get_link(self, v1, v2):
        """ Returns link connecting given vertices """
        return self.__connect_list.get_link(v1, v2)

    # -------------------------------------------------------------------------
    def break_link(self, link):
        """ Breaks given link """
        (v1, v2) = self.__link_list.get_linked_vertices(link)
        self.__link_list.break_link(link)
        self.__connect_list.disconnect(v1, v2)
        self.__adjacency_list.disconnect(v1, v2)

    # -------------------------------------------------------------------------
    def remove_vertex(self, v):
        """ Removes given vertex from the graph """
        connected_vertices = self.__adjacency_list.get_connected_vertices(v)
        for connected_vertex in list(connected_vertices):
            adjacent_link = self.__connect_list.get_link(v, connected_vertex)
            self.__connect_list.disconnect(v, connected_vertex)
            self.__adjacency_list.disconnect(v, connected_vertex)
            self.__link_list.break_link(adjacent_link)

    # -------------------------------------------------------------------------
    def get_connected_vertices(self, v):
        """ Returns set of vertices adjacent to the given one """
        return self.__adjacency_list.get_connected_vertices(v)

    # -------------------------------------------------------------------------
    def get_linked_vertices(self, link):
        """ Returns tuple of vertices for given link """
        return self.__link_list.get_linked_vertices(link)

    # -------------------------------------------------------------------------
    def get_adjacent_links(self, v):
        """ Returns adjacent links for given vertex """
        adjs = self.__adjacency_list.get_connected_vertices(v)
        links = [self.__connect_list.get_link(v, vertex) for vertex in adjs]
        return set(links)

    # -------------------------------------------------------------------------
    def get_all_vertices(self):
        """ Returns all the vertices in the graph """
        return self.__adjacency_list.get_all_vertices()

    # -------------------------------------------------------------------------
    def get_all_links(self):
        """ Returns all the links in the graph """
        return self.__link_list.get_all_links()

'''
Class representing a graph

Created on 06.08.2013
@author: Alexey Bright
'''

class Graph(object):
    ' Represents a graph '

    def __init__(self, nodes = set()):
        ' Constructs a graph '
        self.nodes = {node: set() for node in nodes}
        self.traits = {}
        
    # ----------------------------------------------------------------------- #

    def add_node(self, node, adj_list = set(), trait = None):
        ' Adds node with adjacency list (optionally) to the graph '
        self.nodes[node] = adj_list
        if trait:
            self.traits[node] = trait
        for to_node in self.nodes:
            if to_node in adj_list:
                self.nodes[to_node].add(node)
        
    # ----------------------------------------------------------------------- #
    
    def set_trait(self, node, trait):
        ' Sets trait for given node '
        self.traits[node] = trait
        
    # ----------------------------------------------------------------------- #
    
    def del_node(self, node):
        ' Deletes the specified node '
        del self.nodes[node]
        if node in self.traits:
            del self.traits[node]
        
    # ----------------------------------------------------------------------- #
    
    def connect(self, from_node, to_node):
        ' Connects from_node to to_node '
        self.nodes[from_node].add(to_node)
        self.nodes[to_node].add(from_node)
        
    # ----------------------------------------------------------------------- #
    
    def disconnect(self, from_node, to_node):
        ' Break the link between from_node and to_node '
        self.nodes[from_node].discard(to_node)
        self.nodes[to_node].discard(from_node)
    
    # ----------------------------------------------------------------------- #
    
    def clean(self):
        ' Removes links to non-existant nodes '
        for _, to_nodes in self.nodes.items():
            for to_node in set(to_nodes):
                if to_node not in self.nodes:
                    to_nodes.discard(to_node)
        
    # ----------------------------------------------------------------------- #
    
    def copy(self):
        ' Returns a deep copy of the graph '
        graph = Graph()
        for node, ajd_set in self.nodes.items():
            graph.nodes[node] = ajd_set.copy()
        graph.traits = dict(self.traits)
        return graph
    
    # ----------------------------------------------------------------------- #
    
    def get_connected_nodes(self, node):
        ' Returns connected nodes set '
        return self.nodes[node]
    
    # ----------------------------------------------------------------------- #
    # Sequence interface
    # ----------------------------------------------------------------------- #
    
    def __len__(self):
        return len(self.nodes)
    
    # ----------------------------------------------------------------------- #
    
    def __getitem__(self, node):
        return self.nodes[node], self.traits.get(node, None)
    
    # ----------------------------------------------------------------------- #
    
    def __setitem__(self, node, adj_list):
        self.nodes[node] = adj_list
        for to_node in self.nodes:
            if to_node in adj_list:
                self.nodes[to_node].add(node)
                
    # ----------------------------------------------------------------------- #
        
    def __iter__(self):
        return iter(self.nodes)
    
    # ----------------------------------------------------------------------- #
    
    def __contains__(self, node):
        return node in self.nodes
    
    
    

        
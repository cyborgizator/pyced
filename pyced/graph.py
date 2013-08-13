'''
Class representing a graph

Created on 06.08.2013
@author: Alexey Bright
'''

class Graph(object):
    ' Represents a graph '

    def __init__(self, graph = None):
        ''' Constructs a graph
            @param graph: Graph object to copy or
                          set {n1, n2, n3...) or
                          dict {(n1, n2): e1, (n3, n4): e2... ''' 
        if isinstance(graph, Graph):
            # copy given graph
            self.nodes = {n: adj.copy() for n, adj in graph.nodes.items()}
            self.edges = {(n1, n2): e for (n1, n2), e in graph.edges.items()}
            
        elif isinstance(graph, set):
            # build from set of nodes
            self.nodes = {}
            self.edges = {}
            self.add_disconnected_nodes(graph)
            
        elif isinstance(graph, dict):
            # build from edges dict
            self.nodes = {}
            self.edges = {}
            self.add_edges(graph)
            
        else:
            print 'Incorrect input graph!!!'
            print graph            
    
    # ----------------------------------------------------------------------- #
    
    def add_disconnected_nodes(self, nodes):
        ''' Adds nodes to the graph.
            @param nodes: set {n1, n2, n3...} '''
        self.nodes.update({n: set() for n in nodes})
     
    # ----------------------------------------------------------------------- #
    
    def add_connected_nodes(self, nodes):
        ''' Adds nodes to the graph.
            @param nodes: dict {n1: {adj1}, n2: {adj2}..} '''
        self.nodes.update(nodes)
        for n1, adj in nodes.items():
            for n2 in adj:
                k = order_edge(n1, n2)
                if not self.edges.has_key(k):
                    self.edges[k] = None
    
    # ----------------------------------------------------------------------- #
    
    def add_edges(self, edges):
        ''' Adds edges to the graph
            @param edges: dict {(n1, n2): e} '''
        for (n1, n2), e in edges.items():
            if self.nodes.has_key(n1):
                self.nodes[n1].add(n2)
            else:
                self.nodes[n1] = {n2}
            if self.nodes.has_key(n2):
                self.nodes[n2].add(n1)
            else:
                self.nodes[n2] = {n1}
            self.edges[order_edge(n1, n2)] = e
    
    # ----------------------------------------------------------------------- #
    
    def set_node(self, n, adj = set(), edge = None):
        ' Adds node with adjacency list (optionally) to the graph '
        cp_adj = adj.copy()
        if n in self.nodes:
            # remove edges to/from n
            for bn in (self.nodes[n] - cp_adj):
                self.disconnect(n, bn)
        self.nodes[n] = cp_adj
        for n2 in self.nodes:
            if n2 in cp_adj:
                self.nodes[n2].add(n)
                self.edges[order_edge(n, n2)] = edge
        self.clean()
        
    # ----------------------------------------------------------------------- #    
    
    def del_node(self, n):
        ' Deletes the specified node '
        if n in self.nodes:
            del self.nodes[n]
            self.clean()

    # ----------------------------------------------------------------------- #    
    
    def connect(self, n1, n2, edge = None):
        ' Connects from_node to to_node '
        self.nodes[n1].add(n2)
        self.nodes[n2].add(n1)
        self.edges[order_edge(n1, n2)] = edge
        
    # ----------------------------------------------------------------------- #
    
    def disconnect(self, n1, n2):
        ' Break the link between from_node and to_node '
        self.nodes[n1].discard(n2)
        self.nodes[n2].discard(n1)
        del self.edges[order_edge(n1, n2)]
    
    # ----------------------------------------------------------------------- #
    
    def clean(self):
        ' Removes broken edges '
        for n1, adj in self.nodes.items():
            for n2 in set(adj):
                if n2 not in self.nodes:
                    adj.discard(n2)
                    del self.edges[order_edge(n1, n2)]
    
    # ----------------------------------------------------------------------- #
    
    def get_connected_nodes(self, n):
        ' Returns connected nodes set '
        return self.nodes[n]
    
    # ----------------------------------------------------------------------- #
    
    def fix_adjacency(self):
        ' Fix one-way edges based on correct edges table '
        for n1, n2 in self.edges:
            self.nodes[n1].add(n2)
            self.nodes[n2].add(n1)                
    
    # ----------------------------------------------------------------------- #
    
    def build_edges_table(self):
        ' Builds edges table based on the current adjacency list '
        self.edges = {(n1, n2): None                 
                      for n1, adj in self.nodes.items()
                      for n2 in adj
                      if n1 < n2}    
    
    # ----------------------------------------------------------------------- #
    # Sequence interface
    # ----------------------------------------------------------------------- #
    
    def __len__(self):
        return len(self.nodes)
    
    # ----------------------------------------------------------------------- #
    
    def __getitem__(self, n):
        return self.nodes[n]
    
    # ----------------------------------------------------------------------- #
    
    def __setitem__(self, n, adj):
        self.set_node(n, adj)
                
    # ----------------------------------------------------------------------- #
        
    def __iter__(self):
        return iter(self.nodes)
    
    # ----------------------------------------------------------------------- #
    
    def __contains__(self, n):
        return n in self.nodes
        
# =========================================================================== #

def order_edge(n1, n2):
    return (n1, n2) if n1 < n2 else (n2, n1)

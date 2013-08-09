'''
Class representing a molecular graph

Created on 07.08.2013
@author: Alexey Bright
'''

from collections import OrderedDict
from element import E, Element
from graph import Graph

class MolGraph(Graph):
    ' Represents a molecular graph '
    
    def __init__(self, graph = None):
        ''' Constructs a graph 
            @param graph: Graph object to copy or
                          set {n1, n2, n3...} or
                          dict {n1: {adj1}, n2: {adj2}..} '''
        super(self.__class__, self).__init__(graph)
        self.build_index()
        self.brutto_formula = ''
        self.modified = True
    
    # ----------------------------------------------------------------------- #
    
    def canonicalize(self):
        ' Canonicalizes the molecular graph '
        pass
    
    # ----------------------------------------------------------------------- #
    
    def attach(self, graph, node1, node2):
        ' Connects given graph using locator '
        graph.shift_indices(len(self.nodes))
        self.add_connected_nodes(graph.nodes)
        self.connect(node1, node2)
        self.index.extend(graph.index)
    
    # ----------------------------------------------------------------------- #
    
    def shift_indices(self, d):
        ' Shift indices by d '
        for a in self.nodes:
            a.index += d
    
    # ----------------------------------------------------------------------- #
    
    def replace(self, node, locator):
        ' Replace graph node using locator '
        pass
    
    # ----------------------------------------------------------------------- #
    
    def get_brutto_formula(self):
        ' Returns brutto formula for the molecular graph '
        print 'Modified:', self.modified
        if self.modified:
            # calculate brutto formula
            C_count = 0
            H_count = 0
            other_counts = OrderedDict()
            for a in self.nodes:
                if a.element == E.C:
                    C_count += 1
                elif a.element == E.H:
                    H_count += 1
                else:
                    if a.element.symbol in other_counts:
                        other_counts[a.element.symbol] += 1
                    else:
                        other_counts[a.element.symbol] = 1
            C_part = 'C' + str(C_count) if C_count > 0 else ''
            H_part = 'H' + str(H_count) if H_count > 0 else ''
            others = reduce(lambda b, (e, c): b + e + str(c),
                            other_counts.items(),
                            '')
            self.brutto_formula = C_part + H_part + others
            self.finish()
        return self.brutto_formula
    
    # ----------------------------------------------------------------------- #
    
    def build_index(self):
        ' Builds the index table '
        self.index = [None] * len(self.nodes)
        for a in self.nodes:
            self.index[a.index] = a
    
    # ----------------------------------------------------------------------- #
    
    def modify(self):
        ' Mark the graph as modified '
        self.modified = True
        
    # ----------------------------------------------------------------------- #
    
    def finish(self):
        ' Mark the graph as unmodified '
        self.modified = False
    
    # ----------------------------------------------------------------------- #
    
    def show(self):
        for a in range(0, len(self.index)):
            symbol = self.index[a].element.symbol
            bounds = [x.element.symbol+'(%d)'%(x.index+1) for x in self.get_connected_nodes(self.index[a])]
            print a + 1, '\t-\t', self.index[a].element.symbol, bounds

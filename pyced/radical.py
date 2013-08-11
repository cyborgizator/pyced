'''
Class representing a radical

Created on 18.05.2013
@author: Alexey Bright
'''

from mol_graph import MolGraph

class Radical(object):
    ' Represents a radical '

    def __init__(self, **args):
        ' Constructs a radical '
        
        # extract arguments
        self.radical = args.get('radical')
        self.generator = args.get('generator')
        self.left_radical = args.get('left_radical')
        self.right_radical = args.get('right_radical')
        self.locator = args.get('locator')
        self.bond = args.get('bond')
        
        # create molecular graph based on arguments
        if self.radical:
            # copy given radical
            self.graph = MolGraph(self.radical.graph)
            self.locator = self.radical.locator.copy()
        elif self.left_radical and self.right_radical and self.bond:
            # interconnect given radicals with the bond
            pass
        elif self.generator:
            # build a radical using given generator
            self.graph = MolGraph()
        
        
    # ----------------------------------------------------------------------- #
        
    def set_locator(self, locator):
        ' Sets the current locator '
        pass
    
    # ----------------------------------------------------------------------- #
        
    def add_radical(self, bond, new_radical):
        ' Adds a new radical '
        pass
    
    # ----------------------------------------------------------------------- #
    
    def connect_graph(self, graph):
        ' Connects given graph to the current graph '
        pass
    

    
    
    
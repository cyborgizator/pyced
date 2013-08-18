'''
Class representing a radical

Created on 18.05.2013
@author: Alexey Bright
'''

from modifier import Modifier, Attach
from mol_graph import MolGraph
from locator import Locator
from bond import Bond, SingleBond
from atom import Atom

class Radical(object):
    ' Represents a radical '

    @staticmethod
    def build_from_radical(r, locator = Locator()):
        ' Returns a radical based on given radical and (optionally) locator '
        radical = Radical()
        radical.graph = r.graph
        radical.locator = locator
        return radical
    
    # ----------------------------------------------------------------------- #
    
    @staticmethod
    def build_from_generator(generator):
        ' Returns a radical based on given generator '
        radical = Radical()
        if isinstance(generator, Atom):
            radical.graph = MolGraph({generator.copy()})
            radical.locator = Locator([1])
        else:
            radical.graph = generator.build()
            radical.locator = Locator([generator.get_default_locant()])
        return radical
    # TODO implement locators by default
    
    # ----------------------------------------------------------------------- #
    
    @staticmethod
    def build_from_connection(r1, bond, r2):
        ' Returns a radical based on two given radicals and a chemical bond '
        radical = Radical()
        radical.graph = r1.graph.modify(r1.locator, Attach(r2.graph))
        return radical
        # TODO process bond

    # ----------------------------------------------------------------------- #

    def __init__(self):
        ' Constructs a radical with empty locator and single bond '
        self.locator = Locator()
        self.bond = SingleBond
        
    # ----------------------------------------------------------------------- #
        
    def set_locator(self, locator):
        ' Sets the current locator '
        self.locator = locator
    
    # ----------------------------------------------------------------------- #
    
    def set_bond(self, bond):
        ' Sets the current bond '
        self.bond = bond
    
    # ----------------------------------------------------------------------- #
        
    def add_radical(self, new_radical, bond = SingleBond):
        ' Adds a new radical '
        self.graph.modify(self.locator, Attach(new_radical.graph))
        # TODO process bond
    
    # ----------------------------------------------------------------------- #
    
    def attach(self, graph, bond = SingleBond):
        ' Attaches a molecular graph, atom or generator to the radical '
        self.graph.modify(self.locator, Attach(graph))
        # TODO process bond
    
    # ----------------------------------------------------------------------- #
    
    def connect_graph(self, graph):
        ' Connects given graph to the current graph '
        pass
    

    
    
    
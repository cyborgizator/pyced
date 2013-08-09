'''
Class representing a chemical structure

Created on 15.05.2013
@author: Alexey Bright
'''

from graph import Graph

class Structure(object):
    ' Represents a chemical structure '

    def __init__(self, generator):
        ' Constructs a structure object '
        self.graph = Graph()
    
    # ----------------------------------------------------------------------- #
        
    def create_definition(self):
        ' Returns a chemical structure definition '
        pass
    
    # ----------------------------------------------------------------------- #
    
    def canonicalize(self):
        ' Canonicalizes the molecular graph '
        pass
    
    # ----------------------------------------------------------------------- #
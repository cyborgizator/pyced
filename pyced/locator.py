'''
Class representing a locator

Created on 18.05.2013
@author: Alexey Bright
'''

class Locator(object):
    ' Represents a locator '

    def __init__(self, locants = []):
        ' Constructs a locator '
        self.locants = [x - 1 for x in locants]
        
    # ----------------------------------------------------------------------- #
        
    def append(self, location):
        ' Appends a new location to the locations list '
        self.locants.append(location)
    
    # ----------------------------------------------------------------------- #
    
    def apply_generator(self, graph, generator):
        ' For each locant applies given generator to the molecular graph '
        for locant in self.locants:
            generator.apply(graph, locant)
    
    # ----------------------------------------------------------------------- #
    
    def copy(self):
        ' Returns a deep copy of the locator '
        locator = Locator(self.locants)
        return locator

    # ----------------------------------------------------------------------- #
    # Sequence interface
    # ----------------------------------------------------------------------- #
    
    def __len__(self):
        return len(self.locants)
    
    # ----------------------------------------------------------------------- #
    
    def __getitem__(self, index):
        return self.locants[index]
    
    # ----------------------------------------------------------------------- #
        
    def __iter__(self):
        return iter(self.locants)
    
    # ----------------------------------------------------------------------- #
    
    def __contains__(self, locant):
        return locant in self.locants    
    
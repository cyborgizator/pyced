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
        
    def append(self, locations):
        ' Appends a new locations to the locations list '
        for location in locations:
            self.locants.append(location)
    
    # ----------------------------------------------------------------------- #
    
    def copy(self):
        ' Returns a deep copy of the locator '
        locator = Locator()
        locator.locants = self.locants
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
    
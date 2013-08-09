'''
Class representing a locator

Created on 18.05.2013
@author: Alexey Bright
'''

class Locator(object):
    ' Represents a locator '

    def __init__(self, locations = []):
        ' Constructs a locator '
        self.locations = [x - 1 for x in locations]
        
    # ----------------------------------------------------------------------- #
        
    def append(self, location):
        ' Appends a new location to the locations list '
        self.locations.append(location)
    
    # ----------------------------------------------------------------------- #
    
    def copy(self):
        ' Returns a deep copy of the locator '
        locator = Locator(self.locations)

    # ----------------------------------------------------------------------- #
    # Sequence interface
    # ----------------------------------------------------------------------- #
    
    def __len__(self):
        return len(self.locations)
    
    # ----------------------------------------------------------------------- #
    
    def __getitem__(self, index):
        return self.locations[index]
    
    # ----------------------------------------------------------------------- #
        
    def __iter__(self):
        return iter(self.locations)
    
    # ----------------------------------------------------------------------- #
    
    def __contains__(self, location):
        return location in self.locations    
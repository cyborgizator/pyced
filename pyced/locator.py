'''
Class representing a locator

Created on 18.05.2013
@author: Alexey Bright
'''

class Locator(object):
    ' Represents a locator '

    def __init__(self, location):
        ' Constructs a locator '
        print 'Created locator ', location
        self.location = [location]
        
    # ----------------------------------------------------------------------- #
        
    def append(self, location):
        ' Appends a new location to the locations list '
        self.location.append(location)
    
    # ----------------------------------------------------------------------- #
    
    def copy(self):
        ' Returns a deep copy of the locator '
        pass
'''
Class representing an atom

Created on 09.08.2013
@author: Alexey Bright
'''

class Atom(object):
    ' Represents an atom '
    
    def __init__(self,
                 element,
                 labelled = False,
                 ring = False,
                 index = 0):
        ' Constructs an atom '
        self.element = element
        self.labelled = labelled
        self.ring = ring
        self.index = index
        
    def copy(self):
        print '*** Atom copied'
        atom = Atom(self.element,
                    self.labelled,
                    self.ring,
                    self.index)
        return atom
        
    # ---------------------------------------------------------------------- #
    
    
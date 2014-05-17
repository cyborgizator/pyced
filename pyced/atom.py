'''
Class representing an atom

Created on 09.08.2013
@author: Alexey Bright
'''

from element import E

class Atom(object):
    ' Represents an atom '
    
    def __init__(self,
                 element,
                 labelled = False,
                 ring = False,
                 index = 0,
                 color = -1):
        ' Constructs an atom '
        self.element = element
        self.labelled = labelled
        self.ring = ring
        self.index = index
        if color == -1:
            self.calculate_value()
        
    # ----------------------------------------------------------------------- #
        
    def copy(self):
        ' Returns copy of the atom '
        atom = Atom(self.element,
                    self.labelled,
                    self.ring,
                    self.index,
                    self.color)
        return atom
    
    # ----------------------------------------------------------------------- #
    
    def calculate_value(self):
        ' Calculates comparison value of the atom '
        if self.element == E.H:
            self.value = 0
        else:
            self.value = (1 << 10) if self.element == E.C else 0
            self.value |= (ord('Z') - ord(self.element.symbol[0])) << 5
            if len(self.element.symbol) > 1:
                self.value |= ord('z') - ord(self.element.symbol[1])


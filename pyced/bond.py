'''
Class representing a chemical bond

Created on 18.05.2013
@author: Alexey Bright
'''

class Bond(object):
    ' Represents a chemical bond '

    @classmethod
    def create(cls, symbol):
        bond_types = {'-':  SingleBond,
                      '=':  DoubleBond,
                      '#':  TripleBond,
                      '~':  PiBond,
                      '--': HydrogenBond,
                      '+-': PolarBond,
                      '-+': ReversedPolarBond}        
        if symbol in bond_types:
            return bond_types[symbol]()
        
    # ----------------------------------------------------------------------- #

    def __init__(self):
        ' Constructs a chemical bond '
        print 'Created bond ', self.__class__.__name__
        pass
        
    # ----------------------------------------------------------------------- #
    
    def draw(self, x1, y1, x2, y2): pass    # abstract
        
# =========================================================================== #        
        
class MultipleBond(Bond):
    
    def draw(self, x1, y1, x2, y2, multiplier): pass    # abstract

# =========================================================================== #

class SingleBond(MultipleBond):
    
    def draw(self, x1, y1, x2, y2):
        MultipleBond.draw(self, x1, y1, x2, y2, 1)

# =========================================================================== #

class DoubleBond(MultipleBond):

    def draw(self, x1, y1, x2, y2):
        MultipleBond.draw(self, x1, y1, x2, y2, 2)

# =========================================================================== #

class TripleBond(MultipleBond):

    def draw(self, x1, y1, x2, y2):
        MultipleBond.draw(self, x1, y1, x2, y2, 3)

# =========================================================================== #

class PiBond(Bond): pass

# =========================================================================== #

class HydrogenBond(Bond): pass

# =========================================================================== #

class PolarBond(Bond): pass

# =========================================================================== #

class ReversedPolarBond(Bond): pass

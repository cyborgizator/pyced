'''
Class representing a chemical bond

Created on 18.05.2013
@author: Alexey Bright
'''

class Bond(object):
    ' Represents a chemical bond '

    @classmethod
    def create(cls, symbol, atom1, atom2):
        ''' Creates a bond based on given bond symbol
            @param symbol: is the symbol of bond ('-' single, '=' double etc)
            @param atom1: first bonded atom
            @param atom2: second bonded atom '''  
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

    def __init__(self, atom1, atom2):
        ' Constructs a chemical bond '
        self.atom1 = atom1
        self.atom2 = atom2
        
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

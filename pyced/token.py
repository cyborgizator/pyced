'''
Class, representing a single token

Created on 01.05.2013
@author: Alexey Bright
'''

class Token(object):
    ' Represents a token '

    def __init__(self, text, is_delimiter = False):
        ' Construct a token object '
        self.text = text
        self.is_delimiter = is_delimiter
        
# =========================================================================== #

class BondToken(Token):
    
    def __init__(self, bond_character):
        super(self.__class__, self).__init__(bond_character, False)
        
# =========================================================================== #

class GeneratorToken(Token):
    
    def __init__(self, generator, argument = None):
        Token.__init__(self, generator, False)
        self.argument = argument
        
# =========================================================================== #         
   
class AtomToken(GeneratorToken):
    
    def __init__(self, element_symbol):
        super(self.__class__, self).__init__('atom', False)   
   
# =========================================================================== #     
        
class AtomReplaceToken(GeneratorToken):
    
    def __init__(self, element_symbol):
        super(self.__class__, self).__init__('atom_replace', False)
        
# =========================================================================== #

class LocatorToken(Token):
    
    def __init__(self, number):
        super(self.__class__, self).__init__(number, False)
        self.positions = [int(number)]
        
    # ----------------------------------------------------------------------- #
    
    def append(self, locator):
        length = len(self.positions)
        self.positions[length:] = locator.positions
    
# =========================================================================== #    
    
class RadicalToken(Token):
    
    def __init__(self, argument):
        super(self.__class__, self).__init__(argument.text, False)
        
    
# =========================================================================== #       
    
    
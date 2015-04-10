__author__ = 'Alexey Bright'


class MolecularToken(object):
    """ Represents a token """

    def __init__(self, text, is_delimiter = False):
        """ Construct a token object """
        self.text = text
        self.is_delimiter = is_delimiter


# =============================================================================
class BondToken(MolecularToken):
    
    def __init__(self, bond_character):
        super(self.__class__, self).__init__(bond_character, False)


# =============================================================================
class GeneratorToken(MolecularToken):
    
    def __init__(self, generator, argument = None):
        MolecularToken.__init__(self, generator, False)
        self.argument = argument


# =============================================================================
class AtomToken(GeneratorToken):

    def __init__(self, element_symbol):
        super(self.__class__, self).__init__('atom', False)   


# =============================================================================
class AtomReplaceToken(GeneratorToken):
    
    def __init__(self, element_symbol):
        super(self.__class__, self).__init__('atom_replace', False)


# =============================================================================
class LocatorToken(MolecularToken):
    
    def __init__(self, number):
        super(self.__class__, self).__init__(number, False)
        self.positions = [int(number)]
        
    # -------------------------------------------------------------------------
    def append(self, locator):
        length = len(self.positions)
        self.positions[length:] = locator.positions


# =============================================================================
class RadicalToken(MolecularToken):
    
    def __init__(self, argument):
        super(self.__class__, self).__init__(argument.text, False)

__author__ = 'Alexey Bright'

from graphlib.generic_link import GenericLink


class Bond(GenericLink):
    """ Represents a chemical bond """

    @staticmethod
    def get(symbol):
        """ Returns a bond type based on given bond symbol """
        bond_types = {'-':  SingleBond,
                      '=':  DoubleBond,
                      '#':  TripleBond,
                      '~':  PiBond,
                      '--': HydrogenBond,
                      '+-': PolarBond,
                      '-+': ReversedPolarBond}
        return bond_types[symbol] if symbol in bond_types else Bond

    # -------------------------------------------------------------------------
    @classmethod
    def create(cls, symbol, atom1, atom2):
        """ Creates a bond based on given bond symbol
            :param symbol: is the symbol of bond ('-' single, '=' double etc)
            :param atom1: first bonded atom
            :param atom2: second bonded atom """
        return cls.get(symbol)(atom1, atom2)

    # -------------------------------------------------------------------------
    def __init__(self, atom1, atom2):
        """ Constructs a chemical bond """
        GenericLink.__init__(self)
        self.atom1 = atom1
        self.atom2 = atom2


# =============================================================================
class MultipleBond(Bond):
    pass


# =============================================================================
class SingleBond(MultipleBond):
    pass


# =============================================================================
class DoubleBond(MultipleBond):
    pass


# =============================================================================
class TripleBond(MultipleBond):
    pass


# =============================================================================
class PiBond(Bond):
    pass


# =============================================================================
class HydrogenBond(Bond):
    pass


# =============================================================================
class PolarBond(Bond):
    pass


# =============================================================================
class ReversedPolarBond(Bond):
    pass
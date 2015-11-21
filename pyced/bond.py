__author__ = 'Alexey Bright'

from graphlib.generic_link import GenericLink


class Bond(GenericLink):
    """ Represents a chemical bond """

    # TODO: move CML-related attributes to CML traits
    CML_ORDER = "other"     # code for CML bond representation

    @staticmethod
    def get(symbol):
        """ Returns a bond type based on given bond symbol """
        bond_set = (SingleBond,
                    DoubleBond,
                    TripleBond,
                    PiBond,
                    HydrogenBond,
                    PolarBond,
                    ReversedPolarBond)
        bond_map = {bond_type.SYMBOL: bond_type for bond_type in bond_set}
        return bond_map[symbol] if symbol in bond_map else Bond

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

    CML_ORDER = "S"
    SYMBOL = "-"


# =============================================================================
class DoubleBond(MultipleBond):

    CML_ORDER = "D"
    SYMBOL = "="


# =============================================================================
class TripleBond(MultipleBond):

    CML_ORDER = "T"
    SYMBOL = "#"


# =============================================================================
class PiBond(Bond):

    CML_ORDER = "A"
    SYMBOL = "~"


# =============================================================================
class HydrogenBond(Bond):

    SYMBOL = "--"


# =============================================================================
class PolarBond(Bond):

    SYMBOL = "+-"


# =============================================================================
class ReversedPolarBond(Bond):

    SYMBOL = "-+"

'''
Class representing a generator

Created on 19.05.2013
@author: Alexey Bright
'''

from atom import Atom
from element import E
from bond import SingleBond, PiBond
from mol_graph import MolGraph, order_edge
from helpers import map_subclasses

class Generator(object):
    ' Represents a generator ' 

    @classmethod
    def create(cls, name, arg = None):
        ' Returns a generator or atom by given name '
        if name in cls.generators and arg:
            return cls.generators[name](arg)
        if E.is_element(name) and not arg:
            return Atom(E.get_element(name))
        return cls.generators[name](arg)

    # ----------------------------------------------------------------------- #

    def __init__(self, arg):
        ' Constructs a generator object '
        self.arg = arg

    # ----------------------------------------------------------------------- #
    
    def build(self):
        ' Returns a generated molecular graph '
        return {}

# =========================================================================== #
# Generator Subclasses                                                        #
# =========================================================================== #

class Chain(Generator):
    ' Represetns an aliphatic chain '

    names = {'Chain', 'C'}

    # ----------------------------------------------------------------------- #
    
    def build(self):
        ' Returns a generated molecular graph '
        prev_atom = Atom(E.C, index = 0)
        atom_count = int(self.arg)
        bdic = {} if atom_count > 1 else {prev_atom}
        for i in range(1, atom_count):
            atom = Atom(E.C, index = i)
            bdic[order_edge(prev_atom, atom)] = SingleBond(prev_atom, atom)
            prev_atom = atom
        return MolGraph(bdic)
    
    # ----------------------------------------------------------------------- #
    
    def get_default_locant(self):
        ' Returns default locant for generated radical '
        return 0
        
        # TODO make bond based on syntax

# =========================================================================== #

class Ring(Generator):
    ' Represents an aliphatic cycle '

    names = {'Ring', 'O'}
    bond_type = SingleBond

    # ----------------------------------------------------------------------- #
    
    def build(self):
        ' Returns a generated molecular graph '
        bt = self.__class__.bond_type
        prev_atom = Atom(E.C, index = 0, ring = True)
        bdic = {}
        for i in range(1, int(self.arg)):
            atom = Atom(E.C, index = i, ring = True)
            bdic[order_edge(prev_atom, atom)] = bt(prev_atom, atom)
            prev_atom = atom
        ag = MolGraph(bdic)
        ag.connect(ag.index[0], ag.index[-1], bt(ag.index[0], ag.index[-1]))
        return ag
        
        # TODO exclude repeating code for this, Chain and Arene
        # TODO make bond based on syntax
        
    # ----------------------------------------------------------------------- #
    
    def get_default_locant(self):
        ' Returns default locant for generated radical '
        return 1        
        
# =========================================================================== #

class Arene(Ring):
    ' Represents an arene '

    names = {'Arene', 'Ar'}
    bond_type = PiBond

# =========================================================================== #

class Me(Chain):
    ' Represents a methyl radical '

    names = {'Me', 'CH3'}

# =========================================================================== #

class Et(Chain):
    ' Represents an ethyl radical '

    names = {'Et', 'C2H5'}

# =========================================================================== #

class Ph(Arene):
    ' Represents a phenyl radical '

    names = {'Ph', 'C6H5'}

# =========================================================================== #

class FunctionalGroup(Generator):
    ' Represents a phenyl radical '
    
    names = {'Functional'}
    
    # ----------------------------------------------------------------------- #
    
    def get_default_locant(self):
        ' Returns default locant for generated radical '
        return None
    
# =========================================================================== #

class Nitro(FunctionalGroup):
    ' Represents nitro-group '

    names = {'NO2'}

# =========================================================================== #

class CarboxylicAcid(FunctionalGroup):
    ' Represents carboxylic acid group '

    names = {'COOH'}

# =========================================================================== #

class Nitrile(FunctionalGroup):
    ' Represents nitrile group '

    names = {'CN'}

# =========================================================================== #

class SulfonicAcid(FunctionalGroup):
    ' Represents sulfonic acid '

    names = {'SO3H'}

# =========================================================================== #

Generator.generators = map_subclasses(Generator, vars())


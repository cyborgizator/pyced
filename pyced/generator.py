'''
Class representing a generator

Created on 19.05.2013
@author: Alexey Bright
'''

from atom import Atom
from element import E
from bond import SingleBond, PiBond
from mol_graph import MolGraph, order_edge

class Generator(object):
    ' Represents a generator ' 

    @classmethod
    def create(cls, name, arg = None):
        if name in cls.generators:
            return cls.generators[name](arg)

    # ----------------------------------------------------------------------- #

    @classmethod
    def map_generators(cls, scope):
        ''' Maps all generators in the current scope '''
        cls.generators = {}
        for name, cls_object in scope.items():
            if  isinstance(cls_object, type) and\
                issubclass(cls_object, cls) and\
                cls_object is not cls:
                for name in cls_object.names:
                    cls.generators[name] = cls_object                

    # ----------------------------------------------------------------------- #

    def __init__(self, arg):
        ' Constructs a generator object '
        self.arg = arg

    # ----------------------------------------------------------------------- #

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #
# Generator Subclasses                                                        #
# =========================================================================== #

class AtomAttach(Generator):
    ' Represents an atom radical '

    names = {'atom'}

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        atom = Atom(E.get_element(self.arg), True)
        ag = MolGraph({atom})
        graph.attach(ag, graph.index[locant], atom)

# =========================================================================== #

class AtomReplace(Generator):
    ' Represents an atom replacer '

    names = {'replace'}

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        atom = Atom(E.get_element(self.arg), self.arg != 'C')
        graph.replace(graph.index[locant], atom)

# =========================================================================== #

class Chain(Generator):
    ' Represetns an aliphatic chain '

    names = {'chain'}

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        prev_atom = Atom(E.C, index = 0)
        bdic = {}
        for i in range(1, int(self.arg)):
            atom = Atom(E.C, index = i)
            bdic[order_edge(prev_atom, atom)] = SingleBond(prev_atom, atom)
            prev_atom = atom
        ag = MolGraph(bdic)
        graph.attach(ag, graph.index[locant], ag.index[0])
        

# =========================================================================== #

class Ring(Generator):
    ' Represents an aliphatic cycle '

    names = {'ring', 'o'}
    bond_type = SingleBond

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        bt = self.__class__.bond_type
        prev_atom = Atom(E.C, index = 0)
        bdic = {}
        for i in range(1, int(self.arg)):
            atom = Atom(E.C, index = i)
            bdic[order_edge(prev_atom, atom)] = bt(prev_atom, atom)
            prev_atom = atom
        ag = MolGraph(bdic)
        ag.connect(ag.index[0], ag.index[-1])
        graph.attach(ag, graph.index[locant], ag.index[0])
        # TODO exclude repeating code for this, Chain and Arene

# =========================================================================== #

class Arene(Ring):
    ' Represents an arene '

    names = {'arene', 'ar'}
    bond_type = PiBond

#    def apply(self, graph, locator):
#        ' Applies the generator to given graph using locator object '
#        
#        
#        
#        
#        pass

# =========================================================================== #

class En(Generator):
    ' Represents a double bond replacer '

    names = {'en'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class In(Generator):
    ' Represents a triple bond replacer '

    names = {'in'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Cis(Generator):
    ' Represents a cis-bond modifier '

    names = {'cis'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Trans(Generator):
    ' Represents a trans-bond modifier '

    names = {'trans'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Me(Chain):
    ' Represents a methyl radical '

    names = {'me', 'ch3'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Et(Chain):
    ' Represents an ethyl radical '

    names = {'et', 'c2h5'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass


# =========================================================================== #

class Ph(Arene):
    ' Represents a phenyl radical '

    names = {'ph', 'c6h5'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Nitro(Generator):
    ' Represents nitro-group '

    names = {'no2'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class CarboxylicAcid(Generator):
    ' Represents carboxylic acid group '

    names = {'cooh'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Nitrile(Generator):
    ' Represents nitrile group '

    names = {'cn'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class SulfonicAcid(Generator):
    ' Represents sulfonic acid '

    names = {'so3h'}

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

Generator.map_generators(vars())


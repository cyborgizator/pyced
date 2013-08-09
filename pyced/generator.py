'''
Class representing a generator

Created on 19.05.2013
@author: Alexey Bright
'''

from atom import Atom
from element import E, Element
from mol_graph import MolGraph

class Generator(object):
    ' Represents a generator ' 

    @classmethod
    def create(cls, name, arg = None):
        generators = {'atom'    : AtomConnect,
                      'replace' : AtomReplace,
                      'chain'   : Chain,
                      'ring'    : Ring,
                      'o'       : Ring,
                      'arene'   : Arene,
                      'ar'      : Arene,
                      'en'      : En,
                      'in'      : In,
                      'cis'     : Cis,
                      'trans'   : Trans,
                      'ch3'     : Me,
                      'me'      : Me,
                      'c2h5'    : Et,
                      'et'      : Et,
                      'ph'      : Ph,
                      'no2'     : Nitro,
                      'cooh'    : CarboxylicAcid,
                      'cn'      : Nitrile,
                      'so3h'    : SulfonicAcid}
        if name in generators:
            return generators[name](arg)

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
    
class AtomConnect(Generator):
    ' Represents an atom radical '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        for i in locator:
            atom = Atom(E.get_element(self.arg), True)
            ag = MolGraph({atom})
            graph.attach(ag, graph.index[i], atom)

# =========================================================================== #

class AtomReplace(Generator):
    ' Represents an atom replacer '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        atom = Atom(E.get_element(self.arg), self.arg != 'C')
        ag = MolGraph({atom})
        graph.replace(ag, locator)

# =========================================================================== #

class Chain(Generator):
    ' Represetns an aliphatic chain '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Ring(Generator):
    ' Represents an aliphatic cycle '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Arene(Ring):
    ' Represents an arene '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class En(Generator):
    ' Represents a double bond replacer '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class In(Generator):
    ' Represents a triple bond replacer '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Cis(Generator):
    ' Represents a cis-bond modifier '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Trans(Generator):
    ' Represents a trans-bond modifier '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Me(Chain):
    ' Represents a methyl radical '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Et(Chain):
    ' Represents an ethyl radical '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass


# =========================================================================== #

class Ph(Arene):
    ' Represents a phenyl radical '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Nitro(Generator):
    ' Represents nitro-group '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class CarboxylicAcid(Generator):
    ' Represents carboxylic acid group '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class Nitrile(Generator):
    ' Represents nitrile group '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass

# =========================================================================== #

class SulfonicAcid(Generator):
    ' Represents sulfonic acid '

    def apply(self, graph, locator):
        ' Applies the generator to given graph using locator object '
        pass




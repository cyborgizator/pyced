'''
Class representing a generator

Created on 19.05.2013
@author: Alexey Bright
'''

from atom import Atom
from element import E
from mol_graph import MolGraph

class Generator(object):
    ' Represents a generator ' 

    @classmethod
    def create(cls, name, arg = None):
        generators = {'atom'    : AtomAttach,
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
    
class AtomAttach(Generator):
    ' Represents an atom radical '

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        atom = Atom(E.get_element(self.arg), True)
        ag = MolGraph({atom})
        graph.attach(ag, graph.index[locant], atom)

# =========================================================================== #

class AtomReplace(Generator):
    ' Represents an atom replacer '

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        atom = Atom(E.get_element(self.arg), self.arg != 'C')
        graph.replace(graph.index[locant], atom)

# =========================================================================== #

class Chain(Generator):
    ' Represetns an aliphatic chain '

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        prev_atom = Atom(E.C, index = 0)
        adic = {prev_atom: set()}
        for i in range(1, int(self.arg)):
            atom = Atom(E.C, index = i)
            adic[prev_atom].add(atom)
            adic[atom] = {prev_atom}
            prev_atom = atom            
        ag = MolGraph(adic)
        graph.attach(ag, graph.index[locant], ag.index[0])

# =========================================================================== #

class Ring(Generator):
    ' Represents an aliphatic cycle '

    def apply(self, graph, locant):
        ' Applies the generator to given graph using locator object '
        prev_atom = Atom(E.C, index = 0)
        adic = {prev_atom: set()}
        for i in range(1, int(self.arg)):
            atom = Atom(E.C, index = i)
            adic[prev_atom].add(atom)
            adic[atom] = {prev_atom}
            prev_atom = atom
        # TODO exclude repeating code for this, Chain and Arene
        # TODO exclude repeating loops for locant
        ag = MolGraph(adic)
        ag.connect(ag.index[0], ag.index[-1])
        graph.attach(ag, graph.index[locant], ag.index[0])


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




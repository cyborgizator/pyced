'''
Class representing a generator

Created on 19.05.2013
@author: Alexey Bright
'''

class Generator(object):
    ' Represents a generator ' 

    @classmethod
    def create(cls, name, arg = None):
        generators = {'atom'    : Atom,
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
        pass
    
    # ----------------------------------------------------------------------- #
    
    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass
    
# =========================================================================== #    
    
class Atom(Generator):
    ' Represents an atom radical '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class AtomReplace(Generator):
    ' Represents an atom replacer '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Chain(Generator):
    ' Represetns an aliphatic chain '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Ring(Generator):
    ' Represents an aliphatic cycle '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Arene(Ring):
    ' Represents an arene '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class En(Generator):
    ' Represents a double bond replacer '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class In(Generator):
    ' Represents a triple bond replacer '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Cis(Generator):
    ' Represents a cis-bond modifier '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Trans(Generator):
    ' Represents a trans-bond modifier '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Me(Chain):
    ' Represents a methyl radical '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Et(Chain):
    ' Represents an ethyl radical '
    pass

# =========================================================================== #

class Ph(Arene):
    ' Represents a phenyl radical '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Nitro(Generator):
    ' Represents nitro-group '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class CarboxylicAcid(Generator):
    ' Represents carboxylic acid group '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class Nitrile(Generator):
    ' Represents nitrile group '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass

# =========================================================================== #

class SulfonicAcid(Generator):
    ' Represents sulfonic acid '

    def create_molecular_graph(self):
        ' Creates molecular graph '
        pass




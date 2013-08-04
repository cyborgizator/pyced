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
        print 'Created generator', self.__class__.__name__, '(', arg, ')'
        pass
    
# =========================================================================== #    
    
class Atom(Generator):
    ' Represents an atom radical '
    pass

# =========================================================================== #

class AtomReplace(Generator):
    ' Represents an atom replacer '
    pass

# =========================================================================== #

class Chain(Generator):
    ' Represetns an aliphatic chain '
    pass

# =========================================================================== #

class Ring(Generator):
    ' Represents an aliphatic cycle '
    pass

# =========================================================================== #

class Arene(Ring):
    ' Represents an arene '
    pass

# =========================================================================== #

class En(Generator):
    ' Represents a double bond replacer '
    pass

# =========================================================================== #

class In(Generator):
    ' Represents a triple bond replacer '
    pass

# =========================================================================== #

class Cis(Generator):
    ' Represents a cis-bond modifier '
    pass

# =========================================================================== #

class Trans(Generator):
    ' Represents a trans-bond modifier '
    pass

# =========================================================================== #

class Me(Chain):
    ' Represents a methyl radical '
    pass

# =========================================================================== #

class Et(Chain):
    ' Represents an ethyl radical '
    pass

# =========================================================================== #

class Ph(Arene):
    ' Represents a phenyl radical '
    pass

# =========================================================================== #

class Nitro(Generator):
    ' Represents nitro-group '
    pass

# =========================================================================== #

class CarboxylicAcid(Generator):
    ' Represents carboxylic acid group '
    pass

# =========================================================================== #

class Nitrile(Generator):
    ' Represents nitrile group '
    pass

# =========================================================================== #

class SulfonicAcid(Generator):
    ' Represents sulfonic acid '
    pass
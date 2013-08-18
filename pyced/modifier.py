'''
Class representing a modifier

Created on 14.08.2013
@author: Alexey Bright
'''

from atom import Atom
from element import E
from bond import SingleBond, PiBond
from mol_graph import MolGraph, order_edge
from helpers import map_subclasses

class Modifier(object):
    ' Represents a modifier ' 

    @classmethod
    def create(cls, name, arg = None):
        if name in cls.modifiers:
            return cls.modifiers[name](arg)

    # ----------------------------------------------------------------------- #

    def __init__(self, arg = None):
        ' Constructs a modifier object '
        self.arg = arg

    # ----------------------------------------------------------------------- #

    def apply(self, graph, locant):
        ' Applies the modifier to given graph using locant '
        pass
    
# =========================================================================== #
# Modifier Subclasses                                                         #
# =========================================================================== #

class Attach(Modifier):
    ' Represents attach modifier '

    names = {'attach'}

    def apply(self, graph, locant):
        ' Applies a generator output in arg to given graph using locant '
        if isinstance(self.arg, Atom):
            # argument is an atom
            print 'arg: ', self.arg
            new_graph = MolGraph({self.arg.copy()})
        elif isinstance(self.arg, MolGraph):
            # argument is a molecular graph
            new_graph = self.arg
        else:
            # argument is a generator
            new_graph = self.arg.build()
        print 'contains:'
        new_graph.show()
        graph.attach(new_graph,
                     graph.index[locant],
                     new_graph.index[0],
                     SingleBond)  
        
        # TODO make bond based on syntax  
    
# =========================================================================== #    
    
class Replace(Modifier):
    ' Represents replace modifier '
    
    names = {'replace'}
    
    def apply(self, graph, locant):
        ' Applies a generator output in arg to given graph using locant '
        atom = self.arg
        atom.ring = graph.index[locant]
        graph.replace(graph.index[locant], atom)
    
# =========================================================================== #  

class En(Modifier):
    ' Represents a double bond replacer '

    names = {'en'}

    def apply(self, graph, locant):
        ' Applies the modifier to given graph using locant '
        pass

# =========================================================================== #

class In(Modifier):
    ' Represents a triple bond replacer '

    names = {'in'}

    def apply(self, graph, locant):
        ' Applies the modifier to given graph using locant '
        pass

# =========================================================================== #

class Cis(Modifier):
    ' Represents a cis-bond modifier '

    names = {'cis'}

    def apply(self, graph, locant):
        ' Applies the modifier to given graph using locant '
        pass

# =========================================================================== #

class Trans(Modifier):
    ' Represents a trans-bond modifier '

    names = {'trans'}

    def apply(self, graph, locant):
        ' Applies the modifier to given graph using locant '
        pass

# =========================================================================== #

class Seco(Modifier):
    ' Represents a bond break modifier '
    
    names = {'seco'}
    
    def apply(self, graph, locant):
        ' Applies the modifier to given graph using locant '
        pass        

# =========================================================================== #

Modifier.modifiers = map_subclasses(Modifier, vars())
    
    
'''
Class representing a modifier

Created on 14.08.2013
@author: Alexey Bright
'''

from atom import Atom
from element import E
from bond import SingleBond, DoubleBond, PiBond
from mol_graph import MolGraph, order_edge
from helpers import map_subclasses

class Modifier(object):
    ' Represents a modifier ' 

    @classmethod
    def create(cls, name, **args):
        if name in cls.modifiers:
            return cls.modifiers[name](**args)

    # ----------------------------------------------------------------------- #

    def __init__(self, **args):
        ' Constructs a modifier object '
        self.args = args

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
        ''' Applies a generator output in args["branch"] to given graph using
            locant and bond type in args["bond"] '''
        branch = self.args['branch']
        branch_locant = self.args['locant']

        # branch is an atom
        if isinstance(branch, Atom):
            new_graph = MolGraph({branch.copy()})
          
        # branch is a molecular graph
        elif isinstance(branch, MolGraph):
            new_graph = branch.copy()
            
        # branch is a generator
        else:
            new_graph = branch.build()

        graph.attach(new_graph,
                     graph.index[locant],
                     new_graph.index[branch_locant],
                     self.args['bond'])

# =========================================================================== #    
    
class Replace(Modifier):
    ' Represents replace modifier '
    
    names = {'replace'}
    
    def apply(self, graph, locant):
        ' Replace locant-specified atoms in graph using atom in args["atom"] '
        atom = self.args['atom']
        atom.ring = graph.index[locant]
        graph.replace(graph.index[locant], atom)
    
# =========================================================================== #  

class En(Modifier):
    ' Represents a double bond replacer '

    names = {'en'}

    def apply(self, graph, locant):
        ' Applies the modifier to given graph using locant '
        a1 = graph.index[locant]
        i = self.args.get('to', locant + 2) - 1
        a2 = graph.index[i]
        graph.edges[order_edge(a1, a2)] = DoubleBond(a1, a2)

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

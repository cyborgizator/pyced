"""
Class representing a molecular graph

Created on 07.08.2013
@author: Alexey Bright
"""

from collections import OrderedDict
from element import E
from graph import Graph, order_edge

class MolGraph(Graph):
    ' Represents a molecular graph '
    
    def __init__(self, graph = None):
        ''' Constructs a graph
            @param graph: Graph object to copy or
                          set {n1, n2, n3...) or
                          dict {(n1, n2): e1, (n3, n4): e2... '''
        if graph:
            super(self.__class__, self).__init__(graph)
            self.build_index()         
        self.brutto_formula = ''
        self.modified = True
    
    # ----------------------------------------------------------------------- #
    
    def copy(self):
        ' Returns copy of the graph '
        graph = MolGraph()
        graph.nodes = {}
        graph.edges = {}
        graph.index = [n.copy() for n in self.index]
        for n, adj in self.nodes.items():
            atom = graph.index[n.index]
            graph.nodes[atom] = {graph.index[a.index] for a in adj}
        for (a1, a2), e in self.edges.items():
            atom1 = graph.index[a1.index]
            atom2 = graph.index[a2.index]
            graph.edges[order_edge(atom1, atom2)] = e.__class__(atom1, atom2)
        return graph
    
    # ----------------------------------------------------------------------- #

    def canonicalize(self):
        ' Canonicalizes the molecular graph '
        
        def atom_value_ge(atom1, atom2):
            ' Checks if value(atom1) >= value(atom2) '
            return atom1.value >= atom2.value

        # Step A. Hydrogenless constitution
        
        #    1. Each atom in molecular graph is given numerical "color" in
        #       the following order of precedence (excluding terminal H):
        #            a) Ordering number in the sequence: C, other atoms in
        #               alphabetic order, bridging H.
        #            b) Number of connections (bonds)
        #       Resultant ordered lists of colors presented in order of
        #       the atoms in the CH3CH2CH(Cl)CH3 are:
        #       C:1,1; C:1,2; C:1,3; Cl:2,1; C:1,1  
        def assign_primary_color_lists():
            pass
        
        #    2. Atoms are assigned new colors acording to lexicographical
        #       comparison of the color lists in ascending order:
        #       C:1,1 => 2; C:1,2 = > 3; C: 1,3 => 4; Cl: 2,1 => 5; C:1,1 => 2
        #       Each color is equal to the number of atoms that have this or
        #       smaller color.
        def lexicographical_reassign_colors():
            pass
        
        #    3. Atoms are assigned new ordered lists of colors: the first in
        #       the list is the color of the atom, the rest are sorted in
        #       ascending order colors of the atoms, connected to this atom:
        #       C:2,3; C:3,2,3; C:4,2,3,5; Cl:5,4; C:2,4
        def assign_colored_atoms():
            pass 
        
        #    4. Atoms are assigned new colors according to lexicographical
        #       comparison of the color lists in ascending order:
        #       C:2,3=>1; C:3,2,3=>3; C:4,2,3,5=>4; Cl:5,4=>5; C:2,4=>2
        
        #       call lexicographical_reassign_colors()
        
        #    5. Steps 3-4 are repeated unil all new colors are different or
        #       no more changes occur. The resultant colors produce a so
        #       called equitable partition.
        
        #    6. If some of the colors are still identical, the the smallest
        #       is picked up and reduced to the previous color + 1. For
        #       example, 1,2,5,5,5,7,7 will be 1,2,3,5,5,7,7 and so on.
        def differentiate_colors():
            pass
        
        def check_colors_uniqueness():      # loop condition
            pass
        
        #    7. Repeat steps 3-6 until all colors become different and save
        #       connection table. The process of obtaining the table is split
        #       into 3 steps:
        
        #            a) The connection table is made out of segments, ordered
        #               in ascending order of the color of the first atom in
        #               a segment. The number of the segments is the number
        #               of atoms. Each segment starts with the color of an
        #               atom and is followed by a colon and a sorted list of
        #               the colors of atoms, connected to it:
        #               1:3; 2:4; 3:1,4; 4:2,3,5; 5:4
        
        #            b) Since this connection table contains each connection
        #               two times, it is rewritten by excluding colors that
        #               are greater than the first color in the segment:
        #               1; 2; 3:1; 4:2,3; 5:4
        
        #            c) The delimiters now are redundant because the members
        #               of each segment are always smaller than the first
        #               member of the segment. This is the final connection
        #               table to be saved and used later:
        #               1, 2, 3, 1, 4, 2, 3, 5, 4
        
        #    8. Repeat step 7 for all possible sequences of choosing the atoms
        #       whose color is reduced at step 6. Lexicographically compare
        #       each obtained connection table to the previously saved and
        #       keep the smallest one together with the assignment of the
        #       color to the atoms. These colors are the canonical numbers for
        #       the hydrogenless structure. If two connection tables are
        #       identical then atoms that have same colors in two connection
        #       tables belong to the same equivalence class; this information
        #       is saved and used. The equivalence class is the smallest color
        #       in the equivalence group.
        
        #    9. Make new colors out of the canonical equivalence classes and
        #       repeat steps 3-8 if these colors are different from the colors
        #       previously used at step 3. Obtain the new minimal connection
        #       table. Use these classes as initial colors in the next steps.
        #       If equivalence classes are, for example, 1,1,1,4,4,5,5,5 then
        #       the corresponding colors are 3,3,3,5,5,8,8,8.
        #       
        # Step B. Add hydrogen atoms to the structure
        
        # Step C. Add isotopic composition to the structure
        
        # Step D. Stereochemistry
        
        pass
    
    # ----------------------------------------------------------------------- #
    
    def shift_indices(self, d):
        ' Shift indices by d '
        for a in self.nodes:
            a.index += d    
    
    # ----------------------------------------------------------------------- #
    
    def attach(self, graph, node1, node2, bond_type = None):
        ' Attaches graph via bond between node1 and node2 '
        graph.shift_indices(len(self.nodes))
        self.add_edges(graph.edges)      
        if node2 not in self.nodes:
            self.nodes[node2] = set()
        self.connect(node1, node2, bond_type(node1, node2))
        self.index.extend(graph.index)
    
    # ----------------------------------------------------------------------- #
    
    def replace(self, node1, node2):
        ' Replace graph node1 with node2 '
        self.nodes[node2] = self.nodes[node1]
        for n in self.nodes[node1]:
            self.nodes[n].discard(node1)
            self.nodes[n].add(node2)
            k = order_edge(n, node1)
            e = self.edges[k]
            del self.edges[k]
            self.edges[order_edge(n, node2)] = e
        node2.index = node1.index
        self.index[node1.index] = node2
        del self.nodes[node1]
    
    # ----------------------------------------------------------------------- #
    
    def get_brutto_formula(self):
        ' Returns brutto formula for the molecular graph '
        
        def m_ind(i):
            return str(i) if i > 1 else ''
        
        if self.modified:
            C_count = 0
            H_count = 0
            other_counts = OrderedDict()
            for a in self.nodes:
                if a.element == E.C:
                    C_count += 1
                elif a.element == E.H:
                    H_count += 1
                else:
                    if a.element.symbol in other_counts:
                        other_counts[a.element.symbol] += 1
                    else:
                        other_counts[a.element.symbol] = 1
            C_part = 'C' + m_ind(C_count) if C_count > 0 else ''
            H_part = 'H' + m_ind(H_count) if H_count > 0 else ''
            others = reduce(lambda b, (e, c): b + e + m_ind(c),
                            other_counts.items(),
                            '')
            self.brutto_formula = C_part + H_part + others
            self.modified = False
        return self.brutto_formula
    
    # ----------------------------------------------------------------------- #
    
    def auto_hydrogenize(self):
        ' Automatically calculates hydrogenation of each C-atom '
        for n1, adj in self.nodes.items():
            if n1.element == E.C:
                n1.hydrogenation = 4
                for n2 in adj:
                    index = order_edge(n1, n2)
                    n1.hydrogenation -= self.edges[index].electrons

    # ----------------------------------------------------------------------- #
    
    def build_index(self):
        ' Builds the index table '
        self.index = [None] * len(self.nodes)
        for a in self.nodes:
            self.index[a.index] = a
    
    # ----------------------------------------------------------------------- #
    
    def modify(self, locator, modifier):
        ' For each locant applies given modifier to the molecular graph '
        for locant in locator.locants:
            modifier.apply(self, locant)
        self.modified = True
    
    # ----------------------------------------------------------------------- #
    
    def show(self):
        print 'Index:', self.index
        print 'Nodes:', [(a, a.index, a.element.symbol) for a in self.nodes]
        print 'Edges:', self.edges
        for a in range(0, len(self.index)):
            atom = self.index[a]
            symbol = atom.element.symbol
            bounds = [x.element.symbol+'(%d)'%(x.index+1) for x in self.get_connected_nodes(atom)]
            print a + 1, '\t-\t', symbol, bounds, 'H' + str(atom.hydrogenation), '\t\tring' if atom.ring else '\t\tchain'

        for (a1, a2), e in self.edges.items():
            label = '\t\tring' if a1.ring and a2.ring else '\t\tchain'
            print '(%d, %d)' % (a1.index + 1, a2.index + 1), '=(', a1, ',', a2, ')', e, label

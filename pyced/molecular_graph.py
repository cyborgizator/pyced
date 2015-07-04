__author__ = 'Alexey Bright'

from collections import OrderedDict
from graphlib.generic_graph import GenericGraph
from bond import Bond
from element import E

class MolecularGraph(object):
    """ Represents a molecular graph """

    def __init__(self):
        self._graph = GenericGraph()
        self._atom_index = {}
        self._next_locant = 1
        self.brutto_formula = ''
        self.modified = True

    # -------------------------------------------------------------------------
    def get_atom_count(self):
        return self._graph.get_vertex_count()

    # -------------------------------------------------------------------------
    def get_atoms(self):
        return self._graph.get_all_vertices()

    # -------------------------------------------------------------------------
    def get_bonds(self):
        return self._graph.get_all_links()

    # -------------------------------------------------------------------------
    def set_atom(self, locant, atom):
        atom.set_id(locant)
        self._atom_index[locant] = atom
        self._graph.add_vertex(atom)

    # -------------------------------------------------------------------------
    def add_atom(self, atom):
        """ Adds given atom with the next locant
        :param atom: atom to be added
        :return: next locant value
        """
        self.set_atom(self._next_locant, atom)
        self._next_locant += 1
        return self._next_locant

    # -------------------------------------------------------------------------
    def replace_atom(self, locant, atom):
        # TODO test it
        self._graph.replace_node(self.get_atom_by_locant(locant), atom)
        self._atom_index[locant] = atom

    # -------------------------------------------------------------------------
    def get_atom_by_locant(self, locant):
        return self._atom_index[locant]

    # -------------------------------------------------------------------------
    def add_bond(self, bond):
        self._graph.connect(bond.atom1, bond.atom2, bond)

    # -------------------------------------------------------------------------
    def set_bond(self, locant1, locant2, bond_symbol):
        atom1 = self.get_atom_by_locant(locant1)
        atom2 = self.get_atom_by_locant(locant2)
        bond = Bond.create(bond_symbol, atom1, atom2)
        self._graph.connect(atom1, atom2, bond)

    # -------------------------------------------------------------------------
    def get_brutto_formula(self):
        """ Returns brutto formula for the molecular graph """

        def m_ind(i):
            return str(i) if i > 1 else ""

        if self.modified:
            c_count = 0
            h_count = 0
            other_counts = OrderedDict()
            for a in self.get_atoms():
                if a.element == E.C:
                    c_count += 1
                    connected = len(self._graph.get_connected_vertices(a))
                    h_count += 4 - connected
                elif a.element == E.H:
                    h_count += 1
                else:
                    if a.element.symbol in other_counts:
                        other_counts[a.element.symbol] += 1
                    else:
                        other_counts[a.element.symbol] = 1
            c_part = "C" + m_ind(c_count) if c_count > 0 else ""
            h_part = "H" + m_ind(h_count) if h_count > 0 else ""
            others = reduce(lambda b, (e, c): b + e + m_ind(c),
                            other_counts.items(),
                            "")
            self.brutto_formula = c_part + h_part + others
            self.modified = False
        return self.brutto_formula

__author__ = 'Alexey Bright'

from collections import OrderedDict
from graphlib.generic_graph import GenericGraph
from bond import Bond
from element import E
from atom import Atom

class MolecularGraph(object):
    """ Represents a molecular graph """

    def __init__(self):
        """ Constructs an empty molecular graph """
        self._graph = GenericGraph()
        self._atom_index = {}
        self._next_locant = 1
        self._brutto_formula = ''
        self.modified = True

    # -------------------------------------------------------------------------
    def get_atom_count(self):
        """ Returns number of the atoms in the molecular graph """
        return self._graph.get_vertex_count()

    # -------------------------------------------------------------------------
    def get_neighbors_count(self, atom):
        """ Returns number of the adjacent bonds by given atom """
        return self._graph.get_connected_vertices_count(atom)

    # -------------------------------------------------------------------------
    def get_neighbors(self, atom):
        """ Returns set of connected atoms by the given one """
        return self._graph.get_connected_vertices(atom)

    # -------------------------------------------------------------------------
    def get_atoms(self):
        """ Returns set of all the atoms in the molecular graph """
        return self._graph.get_all_vertices()

    # -------------------------------------------------------------------------
    def get_bonds(self):
        """ Returns set of all the bonds in the molecular graph """
        return self._graph.get_all_links()

    # -------------------------------------------------------------------------
    def get_latest_locant(self):
        """ Returns the latest locant """
        return self._next_locant - 1

    # -------------------------------------------------------------------------
    def set_atom(self, locant, atom):
        """ Sets the atom specified by locant
            :param locant: placement for the atom to be set
            :param atom: atom to be set
        """
        atom.set_id(locant)
        if locant >= self._next_locant:
            self._next_locant = locant + 1
        self._atom_index[locant] = atom
        self._graph.add_vertex(atom)

    # -------------------------------------------------------------------------
    def add_atom(self, atom):
        """ Adds given atom with the next locant
            :param atom: atom to be added
            :return: next locant value
        """
        self.set_atom(self._next_locant, atom)
        return self._next_locant

    # -------------------------------------------------------------------------
    def replace_atom(self, locant, atom):
        """ Replaces the atom specified be locant with another one
            :param locant: placement for atom to be replaced
            :param atom: the new atom
        """
        self._graph.replace_node(self.get_atom_by_locant(locant), atom)
        self._atom_index[locant] = atom

    # -------------------------------------------------------------------------
    def get_atom_by_locant(self, locant):
        """ Returns the atom specified by locant
            :param locant: placement for atom to be returned
            :return: specified atom
        """
        return self._atom_index[locant]

    # -------------------------------------------------------------------------
    def add_bond(self, bond):
        """ Adds given bond to the molecular graph
            :param bond: bond object, referring to the two atoms
        """
        self._graph.connect(bond.atom1, bond.atom2, bond)

    # -------------------------------------------------------------------------
    def set_bond(self, locant1, locant2, bond_symbol):
        """ Creates a bond between atoms specified by given locants
            :param locant1: placement of the first atom
            :param locant2: placement of the second atom
            :param bond_symbol: bond type
        """
        atom1 = self.get_atom_by_locant(locant1)
        atom2 = self.get_atom_by_locant(locant2)
        bond = Bond.create(bond_symbol, atom1, atom2)
        self._graph.connect(atom1, atom2, bond)

    # -------------------------------------------------------------------------
    def attach_molecular_graph(self,
                               locant_from,
                               other,
                               locant_to,
                               bond_symbol):
        """ Attaches given molecular graph to the current one (move contents)
            :param locant_from: place to attach molecular graph
            :param other: molecular graph to be attached
            :param locant_to: place in other graph to attach it
            :param bond_symbol:
        """
        # TODO: test it
        # TODO: re-implement in GenericGraph (?)
        # TODO: replace bond_symbol parameter to bond_type (?)
        atom_from = self.get_atom_by_locant(locant_from)
        atom_to = other.get_atom_by_locant(locant_to)
        for a in range(1, other.get_atom_count() + 1):
            self.add_atom(other.get_atom_by_locant(a))

        for b in other.get_bonds():
            self.add_bond(b)
        bond = Bond.create(bond_symbol, atom_from, atom_to)
        self._graph.connect(atom_from, atom_to, bond)

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
            self._brutto_formula = c_part + h_part + others
            self.modified = False
        return self._brutto_formula

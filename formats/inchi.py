__author__ = 'Alexey Bright'

from generic_format import GenericFormat

class InChI(GenericFormat):

    def canonicalize(self):
        """ Canonicalizes the molecular graph """

        self._current_choice = 0

        # .....................................................................
        def print_colored_list(colored_atoms):
            for color, atom in colored_atoms:
                print color, ":", atom.element.symbol, ", ",
            print

        # .....................................................................
        def atom_value_ge(atom1, atom2):
            """ Checks if value(atom1) >= value(atom2) """
            return atom1.value >= atom2.value

        # .....................................................................
        def assign_primary_color_lists():
            """ Returns initially filled color list for all the atoms """
            return [((a.element.value,
                      self._mg.get_neighbors_count(a)), a)
                    for a in self._mg.get_atoms()]

        # .....................................................................
        def lexicographical_reassign_colors(colored_atoms):
            """ Translates color lists into the new colors """
            sorted_atoms = sorted(colored_atoms, key=lambda item: item[0])
            prev_color = None
            new_color = 0
            recolored_atoms = []
            equiv_class = []
            for color, atom in sorted_atoms:
                if color != prev_color:
                    new_color += 1
                    prev_color = color
                    recolored_atoms +=\
                        [(new_color, a) for a in equiv_class]
                    equiv_class = [atom]
                else:
                    equiv_class.append(atom)
            recolored_atoms +=\
                [(new_color + 1, a) for a in equiv_class]
            return recolored_atoms

        # .....................................................................
        def assign_colored_atoms(colored_atoms):
            """ Creates color lists based on atoms connectivity """
            colored = []
            for color, atom in colored_atoms:
                linked_colors = sorted(c for c in self._mg.get_neighbors(atom))
                colored.append((color,) + tuple(linked_colors))
            return colored

        # .....................................................................
        def differentiate_colors(colored_atoms, skips):
            """ Makes different colors for smallest non-unique color """
            atoms = colored_atoms[:]
            predecessor = 0
            previous = None
            count = skips
            index = -1
            for color, atom in colored_atoms:
                if color == previous:
                    # TODO: fix non-unique enumeration
                    if count == 0:
                        atoms[index] = (predecessor + 1, atoms[index][1])
                        break
                    else:
                        count -= 1
                        index += 1
                        continue
                else:
                    predecessor = previous
                previous = color
                index += 1
            return atoms

        # .....................................................................
        def check_colors_uniqueness(colored_atoms):
            """ Checks if all the colors in the list are different """
            previous = None
            for color, _ in colored_atoms:
                if color == previous:
                    return False
                previous = color
            return True

        atoms = [(1, "a"), (2, "b"), (3, "c"), (5, "d"), (5, "e"), (7, "f"), (7, "g")]

        # Test
        print "Original:", atoms
        print "  Next 0:", differentiate_colors(atoms, 0)
        print "  Next 1:", differentiate_colors(atoms, 1)
        print "  Next 2:", differentiate_colors(atoms, 2)
        print "  Next 3:", differentiate_colors(atoms, 3)
        print "  Next 4:", differentiate_colors(atoms, 4)
        print "  Next 5:", differentiate_colors(atoms, 5)
        return


        # Step A. Hydrogenless constitution

        #    1. Each atom in molecular graph is given numerical "color" in
        #       the following order of precedence (excluding terminal H):
        #            a) Ordering number in the sequence: C, other atoms in
        #               alphabetic order, bridging H.
        #            b) Number of connections (bonds)
        #       Resultant ordered lists of colors presented in order of
        #       the atoms in the CH3CH2CH(Cl)CH3 are:
        #       C:1,1; C:1,2; C:1,3; Cl:2,1; C:1,1
        colored_atoms = assign_primary_color_lists()

        #    2. Atoms are assigned new colors according to lexicographical
        #       comparison of the color lists in ascending order:
        #       C:1,1 => 2; C:1,2 = > 3; C: 1,3 => 4; Cl: 2,1 => 5; C:1,1 => 2
        #       Each color is equal to the number of atoms that have this or
        #       smaller color.
        colored_atoms = lexicographical_reassign_colors(colored_atoms)
        previous_colored_atoms = colored_atoms

        while check_colors_uniqueness(colored_atoms):
            # 3. Atoms are assigned new ordered lists of colors: the first in
            #    the list is the color of the atom, the rest are sorted in
            #    ascending order colors of the atoms, connected to this atom:
            #    C:2,3; C:3,2,3; C:4,2,3,5; Cl:5,4; C:2,4
            colored_atoms = assign_colored_atoms(colored_atoms)

            # 4. Atoms are assigned new colors according to lexicographical
            #    comparison of the color lists in ascending order:
            #    C:2,3=>1; C:3,2,3=>3; C:4,2,3,5=>4; Cl:5,4=>5; C:2,4=>2
            colored_atoms = lexicographical_reassign_colors(colored_atoms)

            # 5. Steps 3-4 are repeated until all new colors are different or
            #    no more changes occur. The resultant colors produce a so
            #    called equitable partition.
            if colored_atoms == previous_colored_atoms:
                # 6. If some of the colors are still identical, then the smallest
                #    is picked up and reduced to the previous color + 1. For
                #    example, 1,2,5,5,5,7,7 will be 1,2,3,5,5,7,7 and so on.
                colored_atoms = differentiate_colors(colored_atoms)



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

        return colored_atoms

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
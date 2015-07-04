__author__ = 'Alexey Bright'

from generic_format import GenericFormat


class MgDebug(GenericFormat):

    # -------------------------------------------------------------------------
    def debug_text(self):
        print "Brutto Formula:", self._mg.get_brutto_formula()
        hr = "-" * 22 + "\n"
        dbg_text = "\nAtoms\n" + hr + "Locant\tElement\tID\n" + hr
        for locant in range(1, self._mg.get_atom_count() + 1):
            atom = self._mg.get_atom_by_locant(locant)
            dbg_text += "%s\t\t%s\t\t%s\n" % (locant,
                                              atom.element.symbol,
                                              atom.get_id())
        dbg_text += "\nBonds\n" + hr + "1st\t\tBond\t2nd\n" + hr
        for bond in self._mg.get_bonds():
            dbg_text += "%s(%s)\t%s\t\t%s(%s)\n" % (bond.atom1.get_id(),
                                                    bond.atom1.element.symbol,
                                                    bond.SYMBOL,
                                                    bond.atom2.get_id(),
                                                    bond.atom2.element.symbol)
        return dbg_text

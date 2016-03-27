from generic_format import GenericFormat
import xml.etree.ElementTree as et

__author__ = 'Alexey Bright'


class Cml(GenericFormat):

    def export(self, molecule_id):
        molecule = et.Element("molecule", {"id": molecule_id})
        atoms = et.Element("atomArray")
        bonds = et.Element("bondArray")
        molecule.append(atoms)
        molecule.append(bonds)

        for atom in self._mg.get_atoms():
            symbol = atom.element.symbol
            atom_node = et.Element("atom", {"id": symbol + str(atom.get_id()),
                                            "elementType": symbol})
            atoms.append(atom_node)

        for bond in self._mg.get_bonds():
            a1_id = bond.atom1.element.symbol + str(bond.atom1.get_id())
            a2_id = bond.atom2.element.symbol + str(bond.atom2.get_id())
            bond_node = et.Element("bond", {"id": a1_id + a2_id,
                                            "atomRefs2": a1_id + " " + a2_id,
                                            "order": bond.CML_ORDER})
            bonds.append(bond_node)

        # TODO: use ElementTree instead to build full XML document
        return et.tostring(molecule)

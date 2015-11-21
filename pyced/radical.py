__author__ = 'Bright'

from locator import Locator
from bond import SingleBond


class Radical:
    """ Represents a radical """

    @staticmethod
    def build_from_generator(generator):
        mg = generator.build()
        # TODO: Improve default locants calculation
        return Radical(mg, locator=Locator([mg.get_latest_locant()]))

    # -------------------------------------------------------------------------
    def __init__(self, mg, locator=None, bond_type=None):
        self.mg = mg
        self.locator = locator if locator else Locator()
        self.bond_type = bond_type if bond_type else SingleBond

    # -------------------------------------------------------------------------
    def set_locator(self, locator):
        self.locator = locator

    # -------------------------------------------------------------------------
    def attach_radical(self, radical, bond_type=None):
        bond_to = bond_type if bond_type else SingleBond
        for locant_from in self.locator:
            self.mg.attach_molecular_graph(locant_from,
                                           radical.mg,
                                           radical.locator.get_first(),
                                           bond_to.SYMBOL)

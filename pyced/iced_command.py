__author__ = 'Alexey Bright'


# Generators
#   Create atom         E
#   Create chain        Chain[n] / C[n]
#   Create cycle        Ring[n] / R[n]
#   Create arene        Arene[n] / Ar[n]
#   Create methyl       Me / CH3
#   Create ethyl        Et / C2H5
#   Create phenyl       Ph / C6H5
#   Create nitro-group  NO2
#   Create carboxyl     COOH
#   Create nitrile      CN
#   Create sulfonyl     SO3H

# Modifiers
#   Replace atom        [E]
#   Make double bond    en
#   Make triple bond    in
#   Make cis-bond       cis
#   Make trans-bond     trans
#   Break bond          seco



class IcedCommand(object):

    def create_atom(self, element, locant):
        pass

    def replace_atom(self, locant1, locant2):
        pass

    def create_bond(self, locant1, locant2, bond_type):
        pass

    def replace_bond(self, locant1, locant2, bond_type):
        pass

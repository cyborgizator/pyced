__author__ = 'Alexey Bright'

from generators.arene import Arene


class Phenyl(Arene):

    names = {'Ph', 'C6H5'}

    def __init__(self, arg = None):
        Arene.__init__(self, 6)

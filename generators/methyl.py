__author__ = 'Alexey Bright'

from generators.chain import Chain


class Methyl(Chain):

    names = {'Me', 'CH3'}

    def __init__(self, arg = None):
        Chain.__init__(self, 1)
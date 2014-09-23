__author__ = 'Alexey Bright'

from generators.chain import Chain


class Ethyl(Chain):

    names = {'Et', 'C2H5'}

    def __init__(self, arg = None):
        Chain.__init__(self, 2)

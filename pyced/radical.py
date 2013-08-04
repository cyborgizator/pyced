'''
Class representing a radical

Created on 18.05.2013
@author: Alexey Bright
'''

class Radical(object):
    ' Represents a radical '

    def __init__(self, **args):
        ' Constructs a radical '
        print 'Created radical ', args
        self.generator = args.get('generator')
        self.radical = args.get('radical')
        self.left_radical = args.get('left_radical')
        self.right_radical = args.get('right_radical')
        self.locator = args.get('locator')
        self.bond = args.get('bond')
        
    def set_locator(self, locator):
        ' Sets the current locator '
        pass
        
    def add_radical(self, bond, new_radical):
        ' Adds a new radical '
        pass
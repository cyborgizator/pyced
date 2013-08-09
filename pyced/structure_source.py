'''
Class, representing a chemical structure source

Created on 01.05.2013
@author: Alexey Bright
'''

import re
from locator import Locator
from radical import Radical 
from bond import Bond
from generator import Generator, AtomConnect, AtomReplace
from errors import StructureParseError

class StructureSource(object):
    ' Represents a chemical structure source '

    def __init__(self, text):
        ' Constructs a chemical structure source object '
        self.length = len(text)
        self.text = text
        self.pos = 0
    
    # ----------------------------------------------------------------------- #
    
    def source(self):
        return self.text[self.pos:]
    
    # ----------------------------------------------------------------------- #
    
    def parse(self):
        ' Parses a structure source to create a structure object '
        pass
    
    # ----------------------------------------------------------------------- #
    
    def pass_whitespace(self):
        ' Passes white space '
        while self.pos < self.length and self.text[self.pos] in ' \n\r\t':
            self.pos += 1
    
    # ----------------------------------------------------------------------- #
    
    def read_character(self, character):
        ' Tries to read a character from the source text '
        self.pass_whitespace()
        if self.pos < self.length and self.text[self.pos] == character:
            self.pos += 1
            return True
        return False
    
    # ----------------------------------------------------------------------- #
    
    def read_regex(self, pattern):
        ' Matches source text against the pattern. Returns text of token '
        self.pass_whitespace()
        matched = re.match(pattern, self.source())
        if matched:
            new_position = self.pos + matched.end()
            token_text = self.text[self.pos:new_position]
            self.pos = new_position        
            return token_text
        return False
    
    # ----------------------------------------------------------------------- #
    
    def read_structure(self):
        ' Tries to read a structure from the source text (?) '
        # structure may be a radical
        return self.read_radical()
    
    # ----------------------------------------------------------------------- #
    
    def read_bond(self):
        ' Tries to read a bond from the source text '
        token_text = self.read_regex(r'-|=|#|\+-|-\+|~|--|:')
        return Bond.create(token_text) if token_text else False
    
    # ----------------------------------------------------------------------- #
    
    def read_radical(self):
        ' Tries to read a radical from the source text '
        radical = False
        # radical may be a generator
        generator = self.read_generator()
        if generator:
            radical = Radical(generator = generator)
        # radical may be bracketed radical
        elif self.read_character('('):
            radical = self.read_radical()
            if not(radical and self.read_character(')')):
                raise StructureParseError
        else:
            return False
        # radical may be followed by a locator prefixed by '-'
        dash = self.read_character('-')
        if dash:
            locator = self.read_locator()
            if locator:
                radical.set_locator(locator)
            # radical may be followed by a chemical bond and a radical
            bond = self.read_bond()
            if bond:
                new_radical = self.read_radical()
                radical.add_radical(bond, new_radical)
        return radical
            
    # ----------------------------------------------------------------------- #
    
    def read_generator(self):
        ' Tries to read a generator from the source text '
        # generator may be ID
        gid = self.read_id()
        if gid:
            # after generator ID may be argument in square brackets
            if self.read_character('['):
                argument = self.read_number()
                if argument and self.read_character(']'):
                    return Generator.create(gid, int(argument))
                raise StructureParseError
            else:
                return Generator.create(gid)
        else:
            # generator can be element symbol
            element = self.read_element()
            if element:
                return AtomConnect(element)
            else:
                # generator can be element symbol in square brackets
                if self.read_character('['):
                    element = self.read_element()
                    if element and self.read_character(']'):
                        return AtomReplace(element)
                    raise StructureParseError
        return False
    
    # ----------------------------------------------------------------------- #
    
    def read_locator(self):
        ' Tries to read a locator from the source text '
        number = self.read_number()
        if number:
            locator = Locator([number])
            if self.read_character(','):
                tail_locator = self.read_locator()
                if tail_locator:
                    locator.append(tail_locator)
            return locator
        return False
    
    # ----------------------------------------------------------------------- #
    
    def read_element(self):
        ' Tries to read an element from the source text '
        return self.read_regex(r'[A-Z][a-z]*')
    
    # ----------------------------------------------------------------------- #
    
    def read_number(self):
        ' Tries to read a number from the source text '
        return self.read_regex(r'[1-9][0-9]*')

    # ----------------------------------------------------------------------- #
  
    def read_id(self):
        ' Tries to read an ID from the source text '
        return self.read_regex(r'[a-z][a-z0-9]*')

    # ----------------------------------------------------------------------- #
    
    
    
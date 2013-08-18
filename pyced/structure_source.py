'''
Class, representing a chemical structure source

Created on 01.05.2013
@author: Alexey Bright
'''

import re
from locator import Locator
from radical import Radical
from atom import Atom
from bond import Bond
from generator import Generator
from modifier import Modifier, Replace
from element import E
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
    
    # B := - | = | # | +- | -+ | ~ | -- | :
    def read_bond(self):
        ' Tries to read a bond from the source text '
        token_text = self.read_regex(r'-|=|#|\+-|-\+|~|--|:')
        return Bond.get(token_text) if token_text else False
            
    # ----------------------------------------------------------------------- #
            
    # R := \(R\) | GR'
    def read_radical(self):
        ' Tries to read a radical from the source text '
        
        def flatten_rs(radical, rs):
            ' Recursively applies R`-tuple to the radical '
            if (len(rs) == 2):
                locator, rsi = rs
                radical.set_locator(locator)
                flatten_rs(radical, rsi)
            elif (len(rs) == 3):
                bond, generator, rsi = rs
                radical.attach(generator, bond)
                flatten_rs(radical, rsi)
        
        radical = False
        # radical may be bracketed
        if self.read_character('('):
            radical = self.read_radical()
            if not(radical and self.read_character(')')):
                raise StructureParseError
        # radical may be generator with following R'-expression
        generator = self.read_generator()
        if generator:
            radical = Radical.build_from_generator(generator)
            rs = self.read_rs()
            flatten_rs(radical, rs)
        return radical
            
    # ----------------------------------------------------------------------- #
    
    # R' := LR' | BGR' | B(GR') | e
    def read_rs(self):
        ' Tries to read a R`-expression from the source text '
        # R' may be locator with following R'-expression
        locator = self.read_locator()
        if locator:
            return (locator, self.read_rs())
        # R' may be bond with following generator and R'-expression
        bond = self.read_bond()
        if bond:
            # TODO insert optional brackets processing
            generator = self.read_generator()
            if generator:
                return (bond, generator, self.read_rs())
        return ()
    
    # TODO process B(GR')
            
    # ----------------------------------------------------------------------- #
    
    # G := Id\[N\] | E | Id
    def read_generator(self):
        ' Tries to read a generator from the source text '
        # generator may be Id (including element symbol)
        gid = self.read_Id()
        if gid:
            # after generator Id may be argument in square brackets
            if self.read_character('['):
                argument = self.read_number()
                if argument and self.read_character(']'):
                    return Generator.create(gid, int(argument))
                raise StructureParseError
            else:
                return Generator.create(gid)
        return False
    
    # ----------------------------------------------------------------------- #
    
    # M := id | \[E\]
    def read_modifier(self):
        ' tries to read a modifier from the source text '
        # modifier may be id
        mid = self.read_id()
        if mid:
            return Modifier.create(mid)
        elif self.read_character('['):
            # modifier may be element symbol in square brackets
            element = self.read_element()
            if element and self.read_character(']'):
                return Replace(Atom(E.get_element(element)))
            raise StructureParseError
        return False
            
    # ----------------------------------------------------------------------- #
    
    # L := N | L,N
    def read_locator(self):
        ' Tries to read a locator from the source text '
        original_pos = self.pos
        self.read_character('-')
        number = self.read_number()
        if number:
            locator = Locator([int(number)])
            if self.read_character(','):
                tail_locator = self.read_locator()
                if tail_locator:
                    locator.append(tail_locator)
            return locator
        self.pos = original_pos
        return False
    
    # ----------------------------------------------------------------------- #
    
    def read_element(self):
        ' Tries to read an element from the source text '
        return self.read_regex(r'[A-Z][a-z]{0-2}')
    
    # ----------------------------------------------------------------------- #
    
    def read_number(self):
        ' Tries to read a number from the source text '
        return self.read_regex(r'[1-9][0-9]*')

    # ----------------------------------------------------------------------- #
  
    def read_id(self):
        ' Tries to read an ID from the source text '
        return self.read_regex(r'[a-z][a-z0-9]*')

    # ----------------------------------------------------------------------- #
    
    def read_Id(self):
        ' Tries to read an ID from the source text '
        return self.read_regex(r'[A-Z][A-Za-z0-9]*')

    # ----------------------------------------------------------------------- #    
    
    def to_read(self):
        print 'To read: ', self.text[self.pos:]
    
    
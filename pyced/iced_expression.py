__author__ = 'Alexey Bright'

import re

from locator import Locator
from radical import Radical
from atom import Atom
from bond import Bond
from generators.generator import Generator
from modifier import Modifier, Replace
from element import E
from errors import StructureParseError


# ICED Syntax
#
# Bond:
#   B ::= - | = | # | +- | -+ | ~ | -- | :
#
# Radical:
#   R ::= (R)T | GT
#
# Tail expression:
#   T ::= LT | MT | BRT | e
#
# Generator:
#   G ::= Id[N] | E | Id | M
#
# Modifier:
#   M ::= id | [E]
#
# Locator:
#   L ::= N | L,N


class IcedExpression(object):
    """ Represents a chemical structure source """

    def __init__(self, text):
        """ Constructs a chemical structure source object """
        self.length = len(text)
        self.text = text
        self.pos = 0
    
    # -------------------------------------------------------------------------
    def source(self):
        return self.text[self.pos:]
    
    # -------------------------------------------------------------------------
    def pass_whitespace(self):
        """ Passes white space """
        while self.pos < self.length and self.text[self.pos] in ' \n\r\t':
            self.pos += 1
    
    # -------------------------------------------------------------------------
    def read_character(self, character):
        """ Tries to read a character from the source text """
        self.pass_whitespace()
        if self.pos < self.length and self.text[self.pos] == character:
            self.pos += 1
            return True
        return False
    
    # -------------------------------------------------------------------------
    def read_regex(self, pattern):
        """ Matches source text against the pattern. Returns text of token """
        self.pass_whitespace()
        matched = re.match(pattern, self.source())
        if matched:
            new_position = self.pos + matched.end()
            token_text = self.text[self.pos: new_position]
            self.pos = new_position        
            return token_text
        return False
    
    # -------------------------------------------------------------------------
    # B ::= - | = | # | +- | -+ | ~ | -- | :
    def read_bond(self):
        """ Tries to read a bond from the source text """
        token_text = self.read_regex(r'-|=|#|\+-|-\+|~|--|:')
        return Bond.get(token_text) if token_text else False
            
    # -------------------------------------------------------------------------
    
    # R ::= (R)T | GT
    def read_radical(self):
        """ Tries to read a radical from the source text """
        radical = False

        # radical may be a generator
        generator = self.read_generator()
        if generator:
            radical = Radical.build_from_generator(generator)
            
        # TODO make unbuilt generator instead of building while parsing
        
        # radical may be bracketed radical following by Tail-expression
        elif self.read_character('('):
            radical = self.read_radical()
            if not(radical and self.read_character(')')):
                raise StructureParseError
        self.read_tail(radical)
        
        return radical

    # -------------------------------------------------------------------------
    # T ::= LT | MT | BRT | e 
    def read_tail(self, radical):
        """ Tries to read a Tail-expression from the source text
            :param radical current radical to apply """

        # T may be a locator with following Tail-expression
        locator = self.read_locator()
        if locator:
            radical.set_locator(locator)
            self.read_tail(radical)
        
        # T may be a modifier with following Tail-expression
        modifier = self.read_modifier()
        if modifier:
            radical.modify(modifier)
            self.read_tail(radical)
        
        # T may be a locator with following radical and Tail-expression
        bond = self.read_bond()
        if bond:
            r = self.read_radical()
            if r:
                radical.attach(r, bond)
            else:
                raise StructureParseError
        
        # At last, T may be empty

    # -------------------------------------------------------------------------
    # G ::= Id[N] | E | Id | M
    def read_generator(self):
        """ Tries to read a generator from the source text """
        
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
    
    # -------------------------------------------------------------------------
    # M ::= id | [E]
    def read_modifier(self):
        """ Tries to read a modifier from the source text """
        
        # modifier is always prefixed with '-'
        original_pos = self.pos
        if self.read_character('-'):
            
            # modifier may be id
            mid = self.read_id()
            if mid:
                return Modifier.create(mid)
            
            # modifier may be element symbol in square brackets
            elif self.read_character('['):
                element = self.read_element()
                if element and self.read_character(']'):
                    return Replace(atom = Atom(E.get_element(element)))
                raise StructureParseError
            
        self.pos = original_pos
        return False

    # -------------------------------------------------------------------------
    # L ::= N | L,N
    def read_locator(self):
        """ Tries to read a locator from the source text """
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
        """ Tries to read an element from the source text """
        return self.read_regex(r'[A-Z][a-z]{0-2}')
    
    # ----------------------------------------------------------------------- #
    def read_number(self):
        """ Tries to read a number from the source text """
        return self.read_regex(r'[1-9][0-9]*')

    # ----------------------------------------------------------------------- #
    def read_id(self):
        """ Tries to read an ID from the source text """
        return self.read_regex(r'[a-z][a-z0-9]*')

    # ----------------------------------------------------------------------- #
    def read_Id(self):
        """ Tries to read an ID from the source text """
        return self.read_regex(r'[A-Z][A-Za-z0-9]*')

    # ----------------------------------------------------------------------- #
    def to_read(self):
        print 'To read: ', self.text[self.pos:]

__author__ = 'Alexey Bright'

from token import Token


class Source(object):
    """ Represents abstract source code """

    def __init__(self,
                 text,
                 delimiters,
                 white_space = (' ', '\n', '\r', '\t')):
        self.text = text
        self.delimiters = delimiters
        self.white_space = white_space
        self.tokens = []

    # -------------------------------------------------------------------------
    def tokenize(self):
        if not self.tokens:
            current_token = ''
            for c in self.text:
                if c in self.white_space:
                    if current_token:
                        self.tokens.append(Token(current_token))
                        current_token = ''
                else:
                    current_token += c
                for delimiter in self.delimiters:
                    length = len(delimiter)
                    token_right = current_token[-length:]
                    if token_right == delimiter:
                        token_left = current_token[:-length]
                        if token_left:
                            self.tokens.append(Token(token_left))
                        self.tokens.append(Token(token_right, True))
                        current_token = ''
                        break
            if current_token:
                self.tokens.append(Token(current_token))
        return self.tokens

'''
Source class, representing source code of PyCED markup
Contains:
    1. Inline equations, for example:
        $(noenum) 3O2 == 2O3
        
    2. Structure equations, for example:
        $ {ph-OH} + Br2 -- {ph-1-OH-2-Br} + HBr^
    
    3. Commands, for example:
        @name({ph}, benzene)

Created on 30.04.2013
@author: Alexey Bright
'''

from source import Source
from final_markup import FinalMarkup

###############################################################################

class PycedSource(Source):
    ' Represents source code of PyCED markup '

    def __init__(self, text, context):
        ' Creates the source object '
        delimiters = ['$', '@']
        super(self.__class__, self).__init__(text, delimiters)
        self.final_markup = None
        self.context = context        
    
    # ----------------------------------------------------------------------- #

    def get_final_markup(self):
        ' Returns an object representing final markup '
        if self.final_markup is None:
            self.build_final_markup()
        return self.final_markup
    
    # ----------------------------------------------------------------------- #

    def build_final_markup(self):
        self.final_markup = FinalMarkup()
        # build
        
    # ----------------------------------------------------------------------- #
    
    def tokenize(self):
        pass
    
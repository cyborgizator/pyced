'''
Source class, representing markup for a single equation
Contains sequence of chemical formulas and the following characters:
        s
+       plus 
=       equal
--      arrow right
==      double arrow (left-right)
^       arrow up
!       arrow down

Created on 01.05.2013
@author: Alexey Bright
'''

class EquationSource(object):
    ' Represents source code of a single equation '

    def __init__(self, text):
        ' Constructs a equation source object '
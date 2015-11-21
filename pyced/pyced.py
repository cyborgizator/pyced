__author__ = 'Alexey Bright'

from generators.generator_factory import GeneratorFactory
from molecular_graph import MolecularGraph
from atom import Atom
from bond import Bond
from element import E
from iced_expression import IcedExpression
from formats.mg_debug import MgDebug
from formats.inchi import InChI


def main():
    # TODO: Make attaching left associative (?)
    expr = IcedExpression("C[4]-2-Cl")
    compound = expr.read_radical()
    dbg_format = MgDebug(compound.mg)
    inchi_format = InChI(compound.mg)
    print inchi_format.canonicalize()
    #print dbg_format.debug_text(), "\n"



if __name__ == '__main__':
    main()

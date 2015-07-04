__author__ = 'Alexey Bright'

from generators.generator_factory import GeneratorFactory
from molecular_graph import MolecularGraph
from atom import Atom
from bond import Bond
from element import E
from formats.mg_debug import MgDebug


def main():
    mg = GeneratorFactory.create("C", 3).build()

    dbg_format = MgDebug(mg)
    print dbg_format.debug_text(), "\n"


if __name__ == '__main__':
    main()

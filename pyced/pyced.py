__author__ = 'Alexey Bright'

import generators
from generators.generator_factory import GeneratorFactory


def main():
    mg = GeneratorFactory.create('Atom', "Xe").build().export_to_cml('xenon')
    print mg


if __name__ == '__main__':
    main()

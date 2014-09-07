__author__ = 'Alexey Bright'

import generators
from generators.generator_factory import GeneratorFactory


def main():
    chain = GeneratorFactory.create('Chain', 3).build().export_to_cml('propane')
    print chain


if __name__ == '__main__':
    main()

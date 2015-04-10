__author__ = 'Alexey Bright'

from generators.generator_factory import GeneratorFactory


def main():
    mg = GeneratorFactory.create('CN', "CN").build().export_to_cml('nitrile')
    print mg


if __name__ == '__main__':
    main()

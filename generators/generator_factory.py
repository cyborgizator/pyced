__author__ = 'Alexey Bright'

from element import E

class GeneratorFactory(object):

    generators = {}

    @classmethod
    def create(cls, name, arg = None):
        if name in cls.generators:
            generator_class = cls.generators[name]
            return generator_class(arg)
        elif E.is_element(name):
            generator_class = cls.generators["Atom"]
            return generator_class(name)

    # -------------------------------------------------------------------------
    @classmethod
    def register_generator(cls, generator_class):
        names = {key: generator_class for key in generator_class.names}
        cls.generators.update(names)


# =============================================================================
class MetaGenerator(type):

    names = None

    def __init__(cls, name, bases, dct):
        type.__init__(cls, name, bases, dct)
        if 'names' in vars(cls):
            cls.names.add(name)
            GeneratorFactory.register_generator(cls)

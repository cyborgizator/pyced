__author__ = 'Alexey Bright'


class ModifierFactory(object):

    modifiers = {}

    @classmethod
    def create(cls, name, **args):
        if name in cls.modifiers:
            modifier_class = cls.modifiers[name]
            return modifier_class(args)

    # -------------------------------------------------------------------------
    @classmethod
    def register_modifier(cls, modifier_class):
        names = {key: modifier_class for key in modifier_class.names}
        cls.modifiers.update(names)


# =============================================================================
class MetaModifier(type):

    names = None

    def __init__(cls, name, bases, dct):
        type.__init__(cls, name, bases, dct)
        if 'names' in vars(cls):
            cls.names.add(name)
            ModifierFactory.register_modifier(cls)

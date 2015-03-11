"""
Helper functions
"""

__author__ = 'Alexey Bright'

import os


# -------------------------------------------------------------------------
def map_subclasses(super_cls, scope):
    """ Maps and returns all the subclasses of cls
        from given vars dictionary """
    sc_map = {}
    for _, cls_obj in scope.items():
        if isinstance(cls_obj, type) and \
                issubclass(cls_obj, super_cls) and \
                cls_obj is not super_cls:
            for name in cls_obj.names:
                sc_map[name] = cls_obj
    return sc_map


# -------------------------------------------------------------------------
def import_all_from(init_path):
    """ Imports all the modules from the specified directory
        :param init_path: path to the directory """
    dn = os.path.dirname(init_path)
    for f in os.listdir(dn):
        if f.endswith('.py') and f != '__init__.py':
            name, ext = os.path.splitext(os.path.basename(f))
            __import__('.'.join((os.path.basename(dn), name)))

'''
Helper functions

Created on 15.08.2013
@author: Alexey Bright
'''

def map_subclasses(super_cls, scope):
    ' Maps and returns all the subclasses of cls from given vars dictionary '
    sc_map = {}
    for _, cls_obj in scope.items():
        if  isinstance(cls_obj, type) and\
            issubclass(cls_obj, super_cls) and\
            cls_obj is not super_cls:
            for name in cls_obj.names:
                sc_map[name] = cls_obj
    return sc_map

# --------------------------------------------------------------------------- #
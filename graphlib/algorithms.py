__author__ = 'Alexey Bright'


def ordered_pair(v1, v2):
    """ Returns ordered pair of vertices """
    if v1 < v2:
        return v1, v2
    else:
        return v2, v1
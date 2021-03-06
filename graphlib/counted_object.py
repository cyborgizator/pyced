__author__ = 'Alexey Bright'


class CountedObject(object):
    """ Represents object having unique ID """

    # -------------------------------------------------------------------------
    def __init__(self):
        self.__class__.__last_id += 1
        self.__id = self.__class__.__last_id

    # -------------------------------------------------------------------------
    def __lt__(self, other):
        """ LESSER THAN operator using IDs comparison """
        return self.__id < other.get_id()

    # -------------------------------------------------------------------------
    def get_id(self):
        """ Returns object's ID """
        return self.__id

    # -------------------------------------------------------------------------
    def set_id(self, id_value):
        """ Sets object's ID """
        self.__id = id_value
    
    # -------------------------------------------------------------------------
    @classmethod
    def reset_id(cls):
        """ Sets objects counter to zero """
        cls.__last_id = 0
    
    __last_id = 0
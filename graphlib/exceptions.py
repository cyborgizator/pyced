__author__ = 'Alexey Bright'


class GraphLibError(Exception):
    """ Represents GraphLib error """
    def __init__(self, message):
        self.__message = message


# =============================================================================
class InvalidLinkError(GraphLibError):
    """ Represents invalid link """
    pass



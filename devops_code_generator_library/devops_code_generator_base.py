"""
This module defines a DevopsCodeGenerator class
which is parent class for all Devops code generator classes
"""


class DevopsCodeGeneratorBase:
    """
    A class representing DevopsCodeGenerator
    which is parent class for all Devops code generator classes
    """

    def __init__(self):
        pass

    def generate(self):
        """
        Generate Devops code
        """

    def __str__(self):
        """
        Return string representation
        """
        return self.__class__.__name__

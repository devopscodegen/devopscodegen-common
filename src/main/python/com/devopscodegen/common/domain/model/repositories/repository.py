"""
This module defines a Repository class representing repositories that contain files
"""


class Repository:
    """
    A class representing a repository that contain files

    Attributes:
        path (str): The path to the repository.
    """

    def __init__(self, path=None):
        """
        Initializes a new instance of the Repository class.

        Args:
            path (str, optional): The path to the repository. Defaults to None.
        """
        self.set_path(path)

    def get_path(self):
        """
        Get the current path of the repository.

        Returns:
            str: The current path of the repository.
        """
        return self.path

    def set_path(self, path=None):
        """
        Set the path of the repository.

        Args:
            path (str, optional): The path to set. Defaults to None.
        """
        self.path = path

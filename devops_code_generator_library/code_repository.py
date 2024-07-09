"""
This module defines a CodeRepository class representing version controlled code repositories,
extending the base Repository class.
"""

from devops_code_generator_library.repository import Repository


class CodeRepository(Repository):
    """
    CodeRepository is a class that extends the Repository class to provide
    additional functionality specific to code repositories.

    Attributes:
        path (str): The file system path to the repository.
    """

    def __init__(self, path=None):
        """
        Initializes a new instance of the CodeRepository class.

        Args:
            path (str, optional): The file system path to the repository. Defaults to None.
        """
        if hasattr(super(), "__init__"):
            super().__init__(path)
        self.path = path

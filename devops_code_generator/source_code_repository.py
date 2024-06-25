"""
This module defines a SourceCodeRepository class for managing source code repositories,
extending functionality from CodeRepository.

Classes:
    SourceCodeRepository: A class representing a source code repository.

Usage:
    source_repo = SourceCodeRepository('/path/to/source/repository')
"""

from devops_code_generator.code_repository import CodeRepository


class SourceCodeRepository(CodeRepository):
    """
    SourceCodeRepository is a class that extends the CodeRepository class to provide
    additional functionality specific to source code repositories.

    Attributes:
        Inherits attributes from CodeRepository.

    Methods:
        __init__(self, path=None): Initializes a new instance of SourceCodeRepository.
    """

    def __init__(self, path=None):
        """
        Initializes a new instance of the SourceCodeRepository class.

        Args:
            path (str, optional): The path to the source code repository. Defaults to None.
        """
        # If the parent class does not have an __init__ method or does not use the path parameter,
        # you can remove the call to super().__init__(path)
        if hasattr(super(), "__init__"):
            super().__init__(path)
        self.path = path

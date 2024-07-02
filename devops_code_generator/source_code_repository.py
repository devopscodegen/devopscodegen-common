"""
This module defines a SourceCodeRepository class for managing source code repositories,
extending functionality from CodeRepository.

Classes:
    SourceCodeRepository: A class representing a source code repository.

Usage:
    source_repo = SourceCodeRepository('/path/to/source/repository')
"""

import os
import logging
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
        self.set_language(None)
        self.set_dependency_manifest(None)
        self.set_dependency_manifest_content(None)
        self.set_dependency_management_tool(None)

    def get_language(self):
        """Get language"""
        return self.language

    def set_language(self, language=None):
        """Set language"""
        self.language = language

    def get_dependency_manifest(self):
        """Get dependency manifest"""
        return self.dependency_manifest

    def set_dependency_manifest(self, dependency_manifest=None):
        """Set dependency manifest"""
        self.dependency_manifest = dependency_manifest

    def get_dependency_manifest_content(self):
        """Get dependency manifest content"""
        return self.dependency_manifest_content

    def set_dependency_manifest_content(self, dependency_manifest_content=None):
        """Set dependency manifest content"""
        self.dependency_manifest_content = dependency_manifest_content

    def get_dependency_management_tool(self):
        """Get dependency management tool"""
        return self.dependency_management_tool

    def set_dependency_management_tool(self, dependency_management_tool=None):
        """Set dependency management tool"""
        self.dependency_management_tool = dependency_management_tool

    def fnd_lang_dep_mfst_dep_mgmt_tool(self):
        """Find language, dependency manifest and dependency management tool"""
        logger = logging.getLogger(__name__)
        language = None
        dependency_manifest = None
        dependency_management_tool = None
        path = self.get_path()
        logger.info(
            "Getting files in root of source code repository directory path %s", path
        )
        files = os.listdir(path)
        if "pom.xml" in files:
            logger.info(
                "pom.xml found in root of source code repository directory path %s",
                path,
            )
            language = "java"
            dependency_manifest = "pom.xml"
            dependency_management_tool = "apache_maven"
        elif "package.json" in files:
            logger.info(
                "package.json found in root of source code repository directory path %s",
                path,
            )
            language = "javascript"
            dependency_manifest = "package.json"
            dependency_management_tool = "npm"
        elif "requirements.txt" in files:
            logger.info(
                "requirements.txt found in root of"
                " source code repository directory path %s",
                path,
            )
            language = "python"
            dependency_manifest = "requirements.txt"
            dependency_management_tool = "pip"
        self.set_language(language)
        self.set_dependency_manifest(dependency_manifest)
        with open(os.path.join(path, dependency_manifest), "r", encoding="utf-8") as f:
            self.set_dependency_manifest_content(f.read())
        self.set_dependency_management_tool(dependency_management_tool)

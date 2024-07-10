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
from devopscodegen_common.repositories.code_repository import (
    CodeRepository,
)
from devopscodegen_common.languages.language import (
    Language,
)
from devopscodegen_common.manifests.dependency_manifest import (
    DependencyManifest,
)
from devopscodegen_common.tools.dependency_management_tool import (
    DependencyManagementTool,
)


class SourceCodeRepository(CodeRepository):
    """
    SourceCodeRepository is a class that extends the CodeRepository class to provide
    additional functionality specific to source code repositories.

    Attributes:
        Inherits attributes from CodeRepository.

    Methods:
        __init__(self, path=None): Initializes a new instance of SourceCodeRepository.
    """

    # pylint: disable=R0913
    def __init__(
        self,
        path: str = None,
        language: Language = None,
        dependency_manifest: DependencyManifest = None,
        dependency_manifest_content: str = None,
        dependency_management_tool: DependencyManagementTool = None,
        middleware: str = None,
    ):
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
        self.set_language(language)
        self.set_dependency_manifest(dependency_manifest)
        self.set_dependency_manifest_content(dependency_manifest_content)
        self.set_dependency_management_tool(dependency_management_tool)
        self.set_middleware(middleware)

    def get_language(self) -> Language:
        """Get language"""
        return self.language

    def set_language(self, language: Language = None):
        """Set language"""
        self.language = language

    def get_dependency_manifest(self) -> DependencyManagementTool:
        """Get dependency manifest"""
        return self.dependency_manifest

    def set_dependency_manifest(self, dependency_manifest: DependencyManifest = None):
        """Set dependency manifest"""
        self.dependency_manifest = dependency_manifest

    def get_dependency_manifest_content(self) -> str:
        """Get dependency manifest content"""
        return self.dependency_manifest_content

    def set_dependency_manifest_content(self, dependency_manifest_content: str = None):
        """Set dependency manifest content"""
        self.dependency_manifest_content = dependency_manifest_content

    def get_dependency_management_tool(self) -> DependencyManagementTool:
        """Get dependency management tool"""
        return self.dependency_management_tool

    def set_dependency_management_tool(
        self, dependency_management_tool: DependencyManagementTool = None
    ):
        """Set dependency management tool"""
        self.dependency_management_tool = dependency_management_tool

    def get_middleware(self) -> str:
        """Get middleware"""
        return self.middleware

    def set_middleware(self, middleware: str = None):
        """Set middleware"""
        self.middleware = middleware

    # pylint: disable=W0718
    def fnd_lang_dep_mfst_dep_mgmt_tool(self):
        """Find language, dependency manifest and dependency management tool"""
        logger = logging.getLogger(__name__)
        language = None
        dependency_manifest = None
        dependency_management_tool = None
        try:
            path = self.get_path()
            logger.info(
                "Getting files in root of source code repository directory path %s",
                path,
            )
            files = os.listdir(path)
            if "pom.xml" in files:
                logger.info(
                    "pom.xml found in root of source code repository directory path %s",
                    path,
                )
                language = Language.JAVA
                dependency_manifest = DependencyManifest.POM_XML
                dependency_management_tool = DependencyManagementTool.APACHE_MAVEN
            elif "package.json" in files:
                logger.info(
                    "package.json found in root of source code repository directory path %s",
                    path,
                )
                language = Language.JAVASCRIPT
                dependency_manifest = DependencyManifest.PACKAGE_JSON
                dependency_management_tool = DependencyManagementTool.NPM
            elif "pyproject.toml" in files and "poetry.lock" in files:
                logger.info(
                    "pyproject.toml and poetry.lock files found in root of"
                    " source code repository directory path %s",
                    path,
                )
                language = Language.PYTHON
                dependency_manifest = DependencyManifest.PYPROJECT_TOML
                dependency_management_tool = DependencyManagementTool.POETRY
            elif "requirements.txt" in files:
                logger.info(
                    "requirements.txt found in root of"
                    " source code repository directory path %s",
                    path,
                )
                language = Language.PYTHON
                dependency_manifest = DependencyManifest.REQUIREMENTS_TXT
                dependency_management_tool = DependencyManagementTool.PIP
            self.set_language(language)
            self.set_dependency_manifest(dependency_manifest)
            if dependency_manifest:
                try:
                    with open(
                        os.path.join(path, dependency_manifest), "r", encoding="utf-8"
                    ) as f:
                        self.set_dependency_manifest_content(f.read())
                except FileNotFoundError:
                    logger.exception(
                        "Dependency manifest file %s not found in %s",
                        dependency_manifest,
                        path,
                    )
                    raise
                except IOError as e:
                    logger.exception(
                        "Error reading dependency manifest file %s in %s: %s",
                        dependency_manifest,
                        path,
                        str(e),
                    )
                    raise
            self.set_dependency_management_tool(dependency_management_tool)

        except Exception as e:
            logger.exception(
                "An error occurred while finding language, dependency manifest,"
                " and dependency management tool: %s",
                str(e),
            )
            raise

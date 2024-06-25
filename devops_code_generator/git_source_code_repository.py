"""
    Module providing a class which represents git source code repository
    of devops code generators.
"""

import os
import tempfile
import git
from devops_code_generator.source_code_repository import SourceCodeRepository


class GitSourceCodeRepository(SourceCodeRepository):
    """Class representing git source code repository of devops code generators."""

    def __init__(self, path=None, url=None, branch=None):
        super().__init__(path)
        self.set_url(url)
        self.set_branch(branch)
        self.set_language(None)
        self.set_dependency_manifest(None)
        self.set_dependency_manifest_content(None)
        self.set_dependency_management_tool(None)

    def get_url(self):
        """Get url"""
        return self.url

    def set_url(self, url=None):
        """Set url"""
        self.url = url

    def get_branch(self):
        """Get branch"""
        return self.branch

    def set_branch(self, branch=None):
        """Set branch"""
        self.branch = branch

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

    def checkout_branch(self):
        """
        Cloning git url branch to source code repository directory path
        if source code repository directory path does not exist already
        """
        path = self.get_path()
        url = self.get_url()
        branch = self.get_branch()
        print("Checking if source code repository directory path exists")
        if path and os.path.exists(path):
            print(
                f"Source code repository directory path {path} already exists."
                " Not checking out git source code repository"
            )
            return
        print("Source code repository directory path does not exist")
        print("Checking if git source code repository url is defined")
        if not url or url == "":
            print(
                "ERROR : Source code repository directory path does not exist"
                " and git source code repository url is not defined"
            )
            return
        print(f"Git source code repository url is defined as {url}")
        print("Checking if git source code repository branch is defined")
        if not branch or branch == "":
            print(
                "ERROR : Source code repository directory path does not exist"
                " and git source code repository branch is not defined"
            )
            return
        print(f"Git source code repository branch is defined as {branch}")
        print("Creating source code repository directory path")
        path = tempfile.mkdtemp()
        print(f"Created source code repository directory path {path}")
        print(
            f"Cloning git url {url} branch {branch}"
            f" to source code repository directory path {path}"
        )
        git.Repo.clone_from(url=url, to_path=path, branch=branch)
        print(
            f"Cloned git url {url} branch {branch}"
            f" to source code repository directory path {path}"
        )
        print(f"Setting source code repository directory path to {path}")
        self.set_path(path)
        print(f"Set source code repository directory path to {path}")

    def fnd_lang_dep_mfst_dep_mgmt_tool(self):
        """Find language, dependency manifest and dependency management tool"""
        language = None
        dependency_manifest = None
        dependency_management_tool = None
        path = self.get_path()
        print(
            f"Getting files in root of git source code repository directory path {path}"
        )
        files = os.listdir(path)
        if "pom.xml" in files:
            print(
                f"pom.xml found in root of git source code repository directory path {path}"
            )
            language = "java"
            dependency_manifest = "pom.xml"
            dependency_management_tool = "apache_maven"
        elif "package.json" in files:
            print(
                f"package.json found in root of git source code repository directory path {path}"
            )
            language = "javascript"
            dependency_manifest = "package.json"
            dependency_management_tool = "npm"
        elif "requirements.txt" in files:
            print(
                f"requirements.txt found in root of"
                f" git source code repository directory path {path}"
            )
            language = "python"
            dependency_manifest = "requirements.txt"
            dependency_management_tool = "pip"
        self.set_language(language)
        self.set_dependency_manifest(dependency_manifest)
        with open(os.path.join(path, dependency_manifest), "r", encoding="utf-8") as f:
            self.set_dependency_manifest_content(f.read())
        self.set_dependency_management_tool(dependency_management_tool)

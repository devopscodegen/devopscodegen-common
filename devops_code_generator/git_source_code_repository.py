"""
    Module providing a class which represents git source code repository
    of devops code generators.
"""

import os
import tempfile
import logging
import git
from devops_code_generator.source_code_repository import SourceCodeRepository


class GitSourceCodeRepository(SourceCodeRepository):
    """Class representing git source code repository of devops code generators."""

    def __init__(self, path=None, url=None, branch=None):
        super().__init__(path)
        self.set_url(url)
        self.set_branch(branch)

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

    def checkout_branch(self):
        """
        Cloning git url branch to source code repository directory path
        if source code repository directory path does not exist already
        """
        logger = logging.getLogger(__name__)
        path = self.get_path()
        url = self.get_url()
        branch = self.get_branch()
        logger.info("Checking if source code repository directory path exists")
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

"""
    Module providing a class which represents git source code repository
    of devops code generators.
"""

import os
import shutil
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

    # pylint: disable=W0718
    def checkout_branch(self):
        """
        Cloning git url branch to source code repository directory path
        if source code repository directory path does not exist already
        """
        logger = logging.getLogger(__name__)
        temp_dir_created = False
        try:
            path = self.get_path()
            url = self.get_url()
            branch = self.get_branch()
            logger.info("Checking if source code repository directory path exists")
            if path and os.path.exists(path):
                logger.info(
                    "Source code repository directory path %s already exists."
                    " Not checking out git source code repository",
                    path,
                )
                return
            logger.info("Source code repository directory path does not exist")
            logger.info("Checking if git source code repository url is defined")
            if not url or url == "":
                logger.info(
                    "ERROR : Source code repository directory path does not exist"
                    " and git source code repository url is not defined"
                )
                return
            logger.info("Git source code repository url is defined as %s", url)
            logger.info("Checking if git source code repository branch is defined")
            if not branch or branch == "":
                logger.info(
                    "ERROR : Source code repository directory path does not exist"
                    " and git source code repository branch is not defined"
                )
                return
            logger.info("Git source code repository branch is defined as %s", branch)
            logger.info("Creating source code repository directory path")
            path = tempfile.mkdtemp()
            temp_dir_created = True
            logger.info("Created source code repository directory path %s", path)
            logger.info(
                "Cloning git url %s branch %s"
                " to source code repository directory path %s",
                url,
                branch,
                path,
            )
            git.Repo.clone_from(url=url, to_path=path, branch=branch)
            logger.info(
                "Cloned git url %s branch %s"
                " to source code repository directory path %s",
                url,
                branch,
                path,
            )
            logger.info("Setting source code repository directory path to %s", path)
            self.set_path(path)
            logger.info("Set source code repository directory path to %s", path)
        except git.GitError as e:
            logger.exception("Git error occurred: %s", str(e))
        except OSError as e:
            logger.exception("OS error occurred: %s", str(e))
        except Exception as e:
            logger.exception("Unexpected error occurred: %s", str(e))
        finally:
            if temp_dir_created:
                logger.info(
                    "Cleaning up temporary source code repository directory path %s",
                    path,
                )
                try:
                    shutil.rmtree(path)
                    logger.info(
                        "Temporary source code repository directory path %s"
                        " deleted successfully",
                        path,
                    )
                except Exception as e:
                    logger.exception(
                        "Failed to delete temporary source code repository"
                        " directory path %s: %s",
                        path,
                        str(e),
                    )

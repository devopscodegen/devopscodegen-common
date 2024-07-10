"""
    Module providing a class which tests the class which represents Git Source Code Repository
    of DevOps Code Generators.
"""

import unittest
import shutil
from unittest.mock import patch

from src.main.python.com.devopscodegen.common.domain.model.repositories.git_source_code_repository import (
    GitSourceCodeRepository,
)


class TestGitSourceCodeRepository(unittest.TestCase):
    """
    Class to unit test the class
    representing Git Source Code Repository of DevOps Code Generators.
    """

    def setUp(self):
        self.repo = GitSourceCodeRepository(
            path="test_path",
            url="https://github.com/spring-projects/spring-petclinic.git",
            branch="main",
        )
        self.repo.set_language("python")
        self.repo.set_dependency_manifest("requirements.txt")
        self.repo.set_dependency_management_tool("pip")

    def test_initialization(self):
        """Test init function"""
        self.assertEqual(self.repo.get_path(), "test_path")
        self.assertEqual(
            self.repo.get_url(),
            "https://github.com/spring-projects/spring-petclinic.git",
        )
        self.assertEqual(self.repo.get_branch(), "main")
        self.assertEqual(self.repo.get_language(), "python")
        self.assertEqual(self.repo.get_dependency_manifest(), "requirements.txt")
        self.assertEqual(self.repo.get_dependency_management_tool(), "pip")

    def test_setters_getters(self):
        """Test get and set functions"""
        self.repo.set_url("https://example.com/new_repo.git")
        self.repo.set_branch("develop")
        self.repo.set_language("java")
        self.repo.set_dependency_manifest("pom.xml")
        self.repo.set_dependency_management_tool("maven")

        self.assertEqual(self.repo.get_url(), "https://example.com/new_repo.git")
        self.assertEqual(self.repo.get_branch(), "develop")
        self.assertEqual(self.repo.get_language(), "java")
        self.assertEqual(self.repo.get_dependency_manifest(), "pom.xml")
        self.assertEqual(self.repo.get_dependency_management_tool(), "maven")

    @patch("os.path.exists")
    @patch("tempfile.mkdtemp", return_value="test_temp_path")
    @patch("git.Repo.clone_from")
    def test_mock_checkout_branch(
        self, mock_clone_from, mock_mkdtemp, mock_path_exists
    ):
        """Mock test checkout_branch function"""
        # Test path already exists
        mock_path_exists.return_value = True
        self.repo.set_path("existing_path")
        self.repo.checkout_branch()
        mock_clone_from.assert_not_called()
        # Test cloning
        mock_path_exists.return_value = False
        self.repo.set_path(None)
        self.repo.checkout_branch()
        mock_clone_from.assert_called_once_with(
            url="https://github.com/spring-projects/spring-petclinic.git",
            to_path=mock_mkdtemp.return_value,
            branch="main",
        )
        self.assertEqual(self.repo.get_path(), mock_mkdtemp.return_value)

    @patch("builtins.open")
    @patch("os.listdir", return_value=["requirements.txt"])
    def test_mock_fnd_lang_dep_mfst_dep_mgmt_tool_python(self, mock_listdir, mock_open):
        """
        Mock test fnd_lang_dep_mfst_dep_mgmt_tool function for
        requirements.txt dependency manifest
        """
        mock_file_content = "Mocked file content"
        mock_open.return_value.__enter__.return_value.read.return_value = (
            mock_file_content
        )
        self.repo.set_path("test_path")
        self.repo.fnd_lang_dep_mfst_dep_mgmt_tool()
        self.assertEqual(self.repo.get_language(), "python")
        self.assertEqual(
            self.repo.get_dependency_manifest(), mock_listdir.return_value[0]
        )
        self.assertEqual(self.repo.get_dependency_manifest_content(), mock_file_content)
        self.assertEqual(self.repo.get_dependency_management_tool(), "pip")

    @patch("builtins.open")
    @patch("os.listdir", return_value=["pom.xml"])
    def test_mock_fnd_lang_dep_mfst_dep_mgmt_tool_java(self, mock_listdir, mock_open):
        """Mock test fnd_lang_dep_mfst_dep_mgmt_tool function for pom.xml dependency manifest"""
        mock_file_content = "Mocked file content"
        mock_open.return_value.__enter__.return_value.read.return_value = (
            mock_file_content
        )
        self.repo.set_path("test_path")
        self.repo.fnd_lang_dep_mfst_dep_mgmt_tool()
        self.assertEqual(self.repo.get_language(), "java")
        self.assertEqual(
            self.repo.get_dependency_manifest(), mock_listdir.return_value[0]
        )
        self.assertEqual(self.repo.get_dependency_manifest_content(), mock_file_content)
        self.assertEqual(self.repo.get_dependency_management_tool(), "apache_maven")

    @patch("builtins.open")
    @patch("os.listdir", return_value=["package.json"])
    def test_mock_fnd_lang_dep_mfst_dep_mgmt_tool_javascript(
        self, mock_listdir, mock_open
    ):
        """
        Mock test fnd_lang_dep_mfst_dep_mgmt_tool function for package.json dependency manifest
        """
        mock_file_content = "Mocked file content"
        mock_open.return_value.__enter__.return_value.read.return_value = (
            mock_file_content
        )
        self.repo.set_path("test_path")
        self.repo.fnd_lang_dep_mfst_dep_mgmt_tool()
        self.assertEqual(self.repo.get_language(), "javascript")
        self.assertEqual(
            self.repo.get_dependency_manifest(), mock_listdir.return_value[0]
        )
        self.assertEqual(self.repo.get_dependency_manifest_content(), mock_file_content)
        self.assertEqual(self.repo.get_dependency_management_tool(), "npm")

    def test_fnd_lang_dep_mfst_dep_mgmt_tool_java(self):
        """Test fnd_lang_dep_mfst_dep_mgmt_tool function with actual git checkout_branch"""
        self.repo.set_path(None)
        self.repo.checkout_branch()
        self.repo.fnd_lang_dep_mfst_dep_mgmt_tool()
        self.assertEqual(self.repo.get_language(), "java")
        self.assertEqual(self.repo.get_dependency_manifest(), "pom.xml")
        self.assertEqual(self.repo.get_dependency_management_tool(), "apache_maven")
        print(
            f"Removing git source code repository directory path {self.repo.get_path()}"
        )
        shutil.rmtree(self.repo.get_path())


if __name__ == "__main__":
    unittest.main()

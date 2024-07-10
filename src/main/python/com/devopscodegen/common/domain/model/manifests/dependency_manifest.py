"""
Dependency Manifest
"""

from enum import Enum


class DependencyManifest(Enum):
    """
    Dependency Manifest
    """

    POM_XML = "pom.xml"
    PACKAGE_JSON = "package.json"
    PYPROJECT_TOML = "pyproject.toml"
    REQUIREMENTS_TXT = "requirements.txt"

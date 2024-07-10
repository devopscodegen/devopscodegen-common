"""
Dependency Manifest
"""

from enum import StrEnum


class DependencyManifest(StrEnum):
    """
    Dependency Manifest
    """

    POM_XML = "pom.xml"
    PACKAGE_JSON = "package.json"
    PYPROJECT_TOML = "pyproject.toml"
    REQUIREMENTS_TXT = "requirements.txt"

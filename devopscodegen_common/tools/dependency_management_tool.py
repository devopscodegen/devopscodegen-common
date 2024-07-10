"""
Dependency management tool
"""

from enum import StrEnum


class DependencyManagementTool(StrEnum):
    """
    Dependency management tool
    """

    APACHE_MAVEN = "apache_maven"
    NPM = "npm"
    POETRY = "poetry"
    PIP = "pip"

"""
Dependency management tool
"""

from enum import Enum


class DependencyManagementTool(Enum):
    """
    Dependency management tool
    """

    APACHE_MAVEN = "apache_maven"
    NPM = "npm"
    POETRY = "poetry"
    PIP = "pip"

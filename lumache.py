"""
Lumache - Python library for the FSS Fox Theme Changer V2 VSCode Extension.
"""

__version__ = "0.1.1"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_kind(kind=None):
    """
    Return a list of random kinds of commands.

    :param kind: Optional "kind" of command.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The commands list.
    :rtype: list[str]
    """
    return ["Change Theme", "placeholder - coming soon", "placeholder - coming soon"]

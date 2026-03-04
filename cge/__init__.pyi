#############################
###                       ###
###          CGE          ###
###                       ###
###       STUB FILE       ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from typing import Callable, Any
from jarbin_toolkit_console.Text import Text


def __getattr__(name: str) -> Any:
    """
    Dynamically retrieve a public attribute from the module namespace.

    Parameters
    ----------
    name : str
        Name of the attribute to retrieve.

    Returns
    -------
    Any
        The requested attribute.

    Raises
    ------
    AttributeError
        If the attribute is not defined in __all__.
    """
    ...

def get_info() -> dict[str, str]:
    """
    Retrieve metadata information about the CGE package.

    Returns
    -------
    dict[str, str]
        Dictionary containing package metadata such as
        name, version, author, license, and description.
    """
    ...

def benchmark(
    function: Callable[..., Any],
    *args: Any,
    **kwargs: Any
) -> tuple[Any, float]:
    """
        Measure execution time of a callable.

        Parameters
        ----------
        function : Callable[..., Any]
            Function to benchmark.

        *args : Any
            Positional arguments passed to the function.

        **kwargs : Any
            Keyword arguments passed to the function.

        Returns
        -------
        tuple[Any, float]
            A tuple containing:
            - The function result
            - The elapsed time in seconds
        """
    ...

def fail(message: str = ...) -> None:
    """
    Raise a CGE Error with a message.

    Parameters
    ----------
    message : str, optional
        Error message to raise.
    """
    ...

def text(*args: Any) -> Text:
    """
    Create a Text object from provided arguments.

    Parameters
    ----------
    *args : Any
        Values converted into a Text instance.

    Returns
    -------
    Text
        Constructed Text object.
    """
    ...


IS_TTY: bool
"""
Indicates whether the current stdout is attached to a TTY.
"""

OS: str
"""
Operating system name as reported by the platform.
"""

TERM: str
"""
Terminal type extracted from environment variables.
"""


__all__: list[str]
"""
Public API symbols exposed by the package.
"""

__author__: str
"""
Package author name.
"""

__email__: str
"""
Author contact email.
"""

__description__: str
"""
Short package description.
"""

__version__: str
"""
Package version string.
"""

__license__: str
"""
Package license identifier.
"""

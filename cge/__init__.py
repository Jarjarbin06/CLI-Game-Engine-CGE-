#############################
###                       ###
###          CGE          ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


## Imports ##
import platform
from os import environ
from sys import stdout
from typing import Callable, Any
from jarbin_toolkit_console.Text import Text
from jarbin_toolkit_time import StopWatch
from jarbin_toolkit_error import Error


## Base Functions ##
def __getattr__(
        name: str
        ) -> dict[str, str]:
    """
        Get the attribute corresponding to "name"
        Raise an AttributeError if the attribute is not found

        Parameters:
            name (str): name of the attribute

        Returns:
            dict[str, str]: attribute
    """

    if name in __all__:
        return globals()[name]
    raise AttributeError(name)


def get_info(
        ) -> dict[str, str]:
    """
        Get info about the Jarbin toolkit

        Returns:
            dict[str, str | dict[str, str]]: info
    """

    return {
        "name": "CGE",
        "description": __description__,
        "version": __version__,
        "subversions": __version__,
        "author": __author__,
        "email": __email__,
        "license": __license__
    }


def benchmark(
        function: Callable,
        *args: Any,
        **kwargs: Any
        ) -> tuple[Any, float]:
    """
    Benchmark the function

    Parameters:
        function (Callable): function to benchmark
        *args (list[Any]): arguments
        **kwargs (dict[str, Any]): keyword arguments

    Returns:
        tuple[Any, float]: benchmark result and elapsed time
    """
    sw = StopWatch(True)
    result = function(*args, **kwargs)
    return result, sw.elapsed()


def fail(
        message: str = "an error occurred"
        ) -> None:
    """
        Raise an Error Exception with a message

        Parameters:
            message (str, optional): message
    """
    raise Error(message)


def text(
        *args: Any
        ) -> Text:
    return Text(list(args))


## Base Variables ##
IS_TTY: bool = stdout.isatty()
OS: str = platform.system()
TERM: str = environ.get("TERM", "")


## API Shortcuts ##
#...


## Special Variables ##
__all__: list[str] = [
    'get_info',
    'benchmark',
    'fail',
    'text',
    'IS_TTY',
    'OS',
    'TERM'
]
__author__: str = 'Nathan Jarjarbin'
__email__: str = 'nathan.amaraggi@epitech.eu'
__description__: str = "CLI Game Engine"
__version__: str = "0.0.1.0"
__license__: str = "GPL"

#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import platform
from os import environ
from sys import stdout

import jarbin_toolkit_console as Console
import jarbin_toolkit_error as Error
import jarbin_toolkit_time as Time

import cge.Data.data_check as Check
import cge.Data.data_transform as Transform
import cge.Data.data_classes as Data
from cge.Error.assertion import ErrorAssertion
from cge.Scene.scene import Scene
from cge.Sprite.sprite import Sprite
from cge.Window.window import Window


def get_info() -> dict[str, str]:
    """
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


def benchmark(function, *args, **kwargs):
    """
    """
    sw = Time.StopWatch(True)
    result = function(*args, **kwargs)
    return result, sw.elapsed()


def fail(message="an error occurred"):
    """
    """
    raise Error.Error(message)


def text(*args):
    """
    """
    return Console.Text.Text(list(args))


IS_TTY = stdout.isatty()
OS = platform.system()
TERM = environ.get("TERM", "")

Animation = Console.Animation

__all__ = [
    'get_info',
    'benchmark',
    'fail',
    'text',
    'IS_TTY',
    'OS',
    'TERM',
    'Window',
    'Scene',
    'Sprite',
    'Data',
    'Transform',
    'Check',
    'Animation',
    'ErrorAssertion'
]
__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__description__ = "CLI Game Engine"
__version__ = "0.0.1.0"
__license__ = "GPL"

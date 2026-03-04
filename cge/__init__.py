#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


## Imports ##
import platform
from os import environ
from sys import stdout
from jarbin_toolkit_console.Text import Text
from jarbin_toolkit_time import StopWatch
from jarbin_toolkit_error import Error


## CGE Imports ##
from cge.Sprite.sprite import Sprite
import cge.Data.data_classes as Data


## API ##
def __getattr__(name):
    if name in __all__:
        return globals()[name]
    raise AttributeError(name)


def get_info() -> dict[str, str]:
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
    sw = StopWatch(True)
    result = function(*args, **kwargs)
    return result, sw.elapsed()


def fail(message="an error occurred"):
    raise Error(message)


def text(*args):
    return Text(list(args))


## Base Variables ##
IS_TTY = stdout.isatty()
OS = platform.system()
TERM = environ.get("TERM", "")

## API Shortcuts ##
# ...


## Special Variables ##
__all__ = [
    'get_info',
    'benchmark',
    'fail',
    'text',
    'IS_TTY',
    'OS',
    'TERM',
    'Data',
    'Sprite'
]
__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__description__ = "CLI Game Engine"
__version__ = "0.0.1.0"
__license__ = "GPL"

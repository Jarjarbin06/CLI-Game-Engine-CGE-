#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################
import inspect

from cge.Data.data_check import assertion
from dataclasses import dataclass

from cge.Data.data_transform import splitANSI


@dataclass
class Vec2:
    x: int
    y: int


@dataclass
class Color:
    r: int
    g: int
    b: int


@dataclass
class Rect:
    x: int
    y: int
    width: int
    height: int

@dataclass
class Char:
    char: str

    def __post_init__(self):
        if not isinstance(self.char, str):
            raise assertion(False, f"invalid type for char", __file__, inspect.currentframe().f_lineno)
        if len(splitANSI(self.char)) != 1:
            raise assertion(False, f"char must be a string of len 1 (len: {len(self.char)})", __file__, inspect.currentframe().f_lineno)

    def __str__(self):
        return self.char

    def __repr__(self):
        return str(self)

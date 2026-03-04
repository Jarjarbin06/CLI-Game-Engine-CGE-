#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


## Imports ##
from dataclasses import dataclass


## API ##
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

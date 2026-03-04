#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from dataclasses import dataclass


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

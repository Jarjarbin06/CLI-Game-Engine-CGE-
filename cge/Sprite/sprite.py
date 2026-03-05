#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import inspect
from types import NoneType
from typing import Any

from jarbin_toolkit_console import Animation
from jarbin_toolkit_time import get_timestamp

from cge.Data.data_check import assertion
from cge.Data.data_classes import *
from cge.Data.data_transform import timestampToId


class Sprite:

    def __init__(self, name: str):
        """
        """
        assertion(isinstance(name, str), "invalid name type", __file__, inspect.currentframe().f_lineno)
        self.sprite_id: int = timestampToId(get_timestamp())
        self.name: str = name
        self.tags: set[str] = set()
        self.animations: dict[str, Animation.Animation] = {"null": Animation.Animation()}
        self.current_animation_key: str = "null"
        self.animation_speed: float = 1.0
        self.frame_index: int = 0
        self.frame_interval: float = 0.0
        self.last_frame_time: int = 0
        self.color_bg: Color = Color(0, 0, 0)
        self.color_fg: Color = Color(0, 0, 0)
        self.dimensions: Vec2 = Vec2(0, 0)
        self.position: Vec2 = Vec2(0, 0)
        self.hitbox: Rect = Rect(0, 0, 0, 0)
        self.anchor: Vec2 = Vec2(0, 0)
        self.z_index: int = 0
        self.render_order: int = 0
        self.render_cache: str = ""
        self.is_enabled: bool = True
        self.is_static: bool = False
        self.is_visible: bool = True
        self.is_flipped_x: bool = False
        self.is_flipped_y: bool = False
        self.is_looping: bool = False
        self.is_playing: bool = True
        self.is_dirty: bool = False
        self.parent: Any | None = None

    def __str__(self):
        """
        """
        if self.is_enabled and self.is_visible:
            return self.render_cache
        return ""

    def setColor(self, color_fg: Color | tuple | None = None, color_bg: Color | tuple | None = None):
        """
        """
        assertion(isinstance(color_fg, Color) or isinstance(color_fg, tuple) or isinstance(color_fg, NoneType), "invalid type for color_fg", __file__, inspect.currentframe().f_lineno)
        assertion(isinstance(color_bg, Color) or isinstance(color_bg, tuple) or isinstance(color_bg, NoneType), "invalid type for color_bg", __file__, inspect.currentframe().f_lineno)

        if isinstance(color_fg, tuple):
            assertion(len(color_fg) == 3, "invalid length of color_fg", __file__, inspect.currentframe().f_lineno)
            color_fg = Color(*color_fg)

        if isinstance(color_bg, tuple):
            assertion(len(color_bg) == 3, "invalid length of color_bg", __file__, inspect.currentframe().f_lineno)
            color_bg = Color(*color_bg)

        if not isinstance(color_fg, NoneType):
            assertion(0 <= color_fg.r <= 255 and 0 <= color_fg.g <= 255 and 0 <= color_fg.b <= 255, "invalid value of RGB for color_fg", __file__, inspect.currentframe().f_lineno)
            self.color_fg = color_fg
            self.is_dirty = True

        if not isinstance(color_bg, NoneType):
            assertion(0 <= color_bg.r <= 255 and 0 <= color_bg.g <= 255 and 0 <= color_bg.b <= 255, "invalid value of RGB for color_bg", __file__, inspect.currentframe().f_lineno)
            self.color_bg = color_bg
            self.is_dirty = True

    def switch_animation(self, name: str):
        """
        """
        assertion(isinstance(name, str), "invalid name type", __file__, inspect.currentframe().f_lineno)
        assertion(name in self.animations, f"sprite not found (name: {name})", __file__, inspect.currentframe().f_lineno)
        self.current_animation_key = name
        self.is_dirty = True

    def add_animation(self, name: str, animation: Animation.Animation):
        """
        """
        assertion(isinstance(name, str), "invalid name type", __file__, inspect.currentframe().f_lineno)
        assertion(isinstance(animation, Animation.Animation), "invalid sprite type", __file__, inspect.currentframe().f_lineno)
        assertion(name not in self.animations, f"sprite already added (name: {name})", __file__, inspect.currentframe().f_lineno)
        self.animations[name] = animation
        self.current_animation_key = name
        self.is_dirty = True

    def render(self):
        """
        """
        if not self.is_enabled:
            self.render_cache = ""
            return
        if self.is_static:
            return
        if self.is_playing:
            self.animations[self.current_animation_key].update()
        self.render_cache = self.animations[self.current_animation_key].render()
        self.is_dirty = False

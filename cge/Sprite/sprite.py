#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from types import NoneType
from jarbin_toolkit_console import Animation
from cge.Data.data_classes import *


class Sprite:

    def __init__(self) -> None:
        self.sprite_id = 0
        self.name = ""
        self.tags = set()
        self.animations = {"base": Animation.Animation()}
        self.current_animation_key = "base"
        self.animation_speed = 1.0
        self.frame_index = 0
        self.frame_interval = 0.0
        self.last_frame_time = 0
        self.color_bg = Color(0, 0, 0)
        self.color_fg = Color(0, 0, 0)
        self.dimensions = Vec2(0, 0)
        self.position = Vec2(0, 0)
        self.hitbox = Rect(0, 0, 0, 0)
        self.anchor = Vec2(0, 0)
        self.z_index = 0
        self.render_order = 0
        self.render_cache = ""
        self.is_enabled = True
        self.is_static = False
        self.is_visible = True
        self.is_flipped_x = False
        self.is_flipped_y = False
        self.is_looping = False
        self.is_playing = False
        self.is_dirty = False
        self.parent = None

    def setColor(self, color_fg=None, color_bg=None) -> None:
        assert isinstance(color_fg, Color) or isinstance(color_fg, tuple) or isinstance(color_fg, NoneType), "invalid type for color_fg"
        assert isinstance(color_bg, Color) or isinstance(color_bg, tuple) or isinstance(color_bg, NoneType), "invalid type for color_bg"

        if isinstance(color_fg, tuple):
            assert len(color_fg) == 3, "invalid length of color_fg"
            color_fg = Color(*color_fg)

        if isinstance(color_bg, tuple):
            assert len(color_bg) == 3, "invalid length of color_bg"
            color_bg = Color(*color_bg)

        if not isinstance(color_fg, NoneType):
            assert 0 <= color_fg.r <= 255 and 0 <= color_fg.g <= 255 and 0 <= color_fg.b <= 255, "invalid value of RGB for color_fg"
            self.color_fg = color_fg
            self.is_dirty = True

        if not isinstance(color_bg, NoneType):
            assert 0 <= color_bg.r <= 255 and 0 <= color_bg.g <= 255 and 0 <= color_bg.b <= 255, "invalid value of RGB for color_bg"
            self.color_bg = color_bg
            self.is_dirty = True

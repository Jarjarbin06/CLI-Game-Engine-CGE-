import pytest


from cge import Sprite
from cge import Data


def test_sprite_attributes(
        ) -> None:
    sprite = Sprite()
    assert hasattr(sprite, "sprite_id")
    assert hasattr(sprite, "name")
    assert hasattr(sprite, "tags")
    assert hasattr(sprite, "animations")
    assert hasattr(sprite, "current_animation_key")
    assert hasattr(sprite, "animation_speed")
    assert hasattr(sprite, "frame_index")
    assert hasattr(sprite, "frame_interval")
    assert hasattr(sprite, "last_frame_time")
    assert hasattr(sprite, "color_bg")
    assert hasattr(sprite, "color_fg")
    assert hasattr(sprite, "dimensions")
    assert hasattr(sprite, "position")
    assert hasattr(sprite, "hitbox")
    assert hasattr(sprite, "anchor")
    assert hasattr(sprite, "z_index")
    assert hasattr(sprite, "render_order")
    assert hasattr(sprite, "render_cache")
    assert hasattr(sprite, "is_enabled")
    assert hasattr(sprite, "is_static")
    assert hasattr(sprite, "is_visible")
    assert hasattr(sprite, "is_flipped_x")
    assert hasattr(sprite, "is_flipped_y")
    assert hasattr(sprite, "is_looping")
    assert hasattr(sprite, "is_playing")
    assert hasattr(sprite, "is_dirty")
    assert hasattr(sprite, "parent")


def test_sprite_setColor(
        ) -> None:

    sprite_1 = Sprite()
    sprite_1.setColor(Data.Color(255, 0, 0))
    assert isinstance(sprite_1.color_fg, Data.Color)
    assert sprite_1.color_fg.r == 255 and sprite_1.color_fg.g == sprite_1.color_fg.g == 0

    sprite_2 = Sprite()
    sprite_2.setColor((255, 0, 0))
    assert isinstance(sprite_2.color_fg, Data.Color)
    assert sprite_2.color_fg.r == 255 and sprite_2.color_fg.g == sprite_2.color_fg.g == 0

    sprite_3 = Sprite()
    sprite_3.setColor(None, Data.Color(255, 0, 0))
    assert isinstance(sprite_3.color_bg, Data.Color)
    assert sprite_3.color_bg.r == 255 and sprite_3.color_bg.g == sprite_3.color_bg.g == 0

    sprite_4 = Sprite()
    sprite_4.setColor(None, (255, 0, 0))
    assert isinstance(sprite_4.color_bg, Data.Color)
    assert sprite_4.color_bg.r == 255 and sprite_4.color_bg.g == sprite_4.color_bg.g == 0

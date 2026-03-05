#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import inspect
from typing import Any

from jarbin_toolkit_time import get_timestamp

from cge.Data.data_classes import Char
from cge.Data.data_check import assertion
from cge.Data.data_transform import timestampToId, splitANSI
from cge.Sprite.sprite import Sprite


class Scene:

    def __init__(self, name: str):
        """
        """
        assertion(isinstance(name, str), "invalid name type", __file__, inspect.currentframe().f_lineno)
        self.scene_id: int = timestampToId(get_timestamp())
        self.name: str = name
        self.tags: set[str] = set()
        self.sprites: dict[int, Sprite] = {}
        self.is_dirty: bool = True
        self.render_scene_cache: list[list[Char]] = []
        self.parent: Any | None = None

    def __str__(self):
        """
        """
        string: str = ""
        for line in self.render_scene_cache:
            string += str(line) + "\n"
        return string

    def check_dirty(self):
        """
        """
        for sprite in self.sprites.values():
            if sprite.is_dirty:
                self.is_dirty = True
        return self.is_dirty

    def add_sprite(self, sprite: Sprite):
        """
        """
        assertion(isinstance(sprite, Sprite), "invalid sprite type", __file__, inspect.currentframe().f_lineno)
        assertion(sprite.sprite_id not in self.sprites, f"sprite already added (id: {sprite.sprite_id})", __file__, inspect.currentframe().f_lineno)
        self.sprites[sprite.sprite_id] = sprite
        sprite.parent = self
        self.is_dirty = True

    def _convert_string(self, string: str):
        """
        """
        string: str
        for sprite in self.sprites.values():
            string = str(sprite)
            print([Char(char) for char in splitANSI(string)])

    def render(self):
        """
        """
        if not (self.parent and self.render_scene_cache) :
            return
        for sprite in self.sprites.values():
            sprite.render()
        for layer in range(0, 10):
            for order in range(len(self.sprites)):
                for sprite in self.sprites.values():
                    if sprite.z_index == layer and sprite.render_order == order:
                        self._convert_string(str(sprite))
        self.is_dirty = False

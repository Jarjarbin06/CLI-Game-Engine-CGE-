#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import inspect

from jarbin_toolkit_console import Console
from jarbin_toolkit_time import Time

from cge.Data.data_check import assertion
from cge.Data.data_classes import Char, Vec2
from cge.Scene.scene import Scene


class Window:

    def __init__(self):
        """
        """
        self.scenes: dict[int, Scene] = {}
        self.current_scene_key: int = -1
        self.size: Vec2 = Vec2(100, 10)
        self.render_window_cache: list[list[Char]] = [[Char(" ") for _ in range(self.size.x)] for _ in range(self.size.y)]
        # self.event : Event = None
        self.is_dirty: bool = False

    def __str__(self):
        """
        """
        string: str = ""
        for line in self.render_window_cache:
            string += line + "\n"
        return string

    def check_dirty(self):
        """
        """
        for scene in self.scenes.values():
            if scene.check_dirty():
                self.is_dirty = True
        return self.is_dirty

    def add_scene(self, scene: Scene):
        """
        """
        assertion(isinstance(scene, Scene), "invalid scene type", __file__, inspect.currentframe().f_lineno)
        assertion(scene.scene_id not in self.scenes, f"scene already added (id: {scene.scene_id})", __file__, inspect.currentframe().f_lineno)
        scene.render_scene_cache = [[Char(" ") for _ in range(self.size.x)] for _ in range(self.size.y)]
        self.scenes[scene.scene_id] = scene
        self.current_scene_key = scene.scene_id
        scene.parent = self
        self.is_dirty = True

    def switch_scene(self, name: str):
        """
        """
        assertion(isinstance(name, str), "invalid name type", __file__, inspect.currentframe().f_lineno)
        for scene_id in self.scenes:
            if self.scenes[scene_id].name == name:
                self.current_scene_key = scene_id
                self.is_dirty = True
                return
        assertion(False, f"sprite not found (name: {name})", __file__, inspect.currentframe().f_lineno)

    def render(self):
        for line in range(self.size.y):
            for column in range(self.size.x):
                self.render_window_cache[line][column] = self.scenes[self.current_scene_key].render_scene_cache[line][column]

    def draw(self):
        """
        """
        Console.execute("clear || clean || cls")
        if self.current_scene_key != -1:
            for line in range(self.size.y):
                for column in range(self.size.x):
                    Console.print(str(self.scenes[self.current_scene_key].render_scene_cache[line][column]), end="")
                Console.print()
        Time.wait(0.5)

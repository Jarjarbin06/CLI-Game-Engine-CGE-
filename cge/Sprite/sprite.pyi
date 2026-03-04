#############################
###                       ###
###          CGE          ###
###                       ###
###       STUB FILE       ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from typing import Any
from jarbin_toolkit_console import Animation
from cge.Data.data_classes import Vec2, Color, Rect


class Sprite:
    """
    Renderable ASCII / ANSI sprite entity.

    This object represents a drawable element that supports
    hierarchy, animation, coloring, flipping, and collision.

    Attributes
    ----------
    sprite_id : int
        Unique identifier of the sprite.

    name : str
        Human-readable name.

    tags : set[str]
        Arbitrary classification labels.

    parent : Any | None
        Parent object in the scene graph.

    position : Vec2
        Position in the scene (x, y).

    anchor : Vec2
        Pivot point inside the sprite (x, y).

    dimensions : Vec2
        Width and height in characters.

    z_index : int
        Layer priority.

    render_order : int
        Secondary sorting value.

    color_fg : Color
        Foreground RGB color.

    color_bg : Color
        Background RGB color.

    is_visible : bool
        Rendering visibility flag.

    is_flipped_x : bool
        Horizontal mirroring flag.

    is_flipped_y : bool
        Vertical mirroring flag.

    render_cache : str
        Cached rendered string.

    is_dirty : bool
        True when cache must be regenerated.

    animations : dict[str, Animation]
        Available animations.

    current_animation_key : str
        Active animation identifier.

    animation_speed : float
        Playback speed multiplier.

    frame_index : int
        Current frame index.

    frame_interval : float
        Time between frames (seconds).

    last_frame_time : float
        Timestamp of last frame update.

    is_looping : bool
        Whether animation loops.

    is_playing : bool
        Whether animation is currently playing.

    hitbox : Rect
        Bounding box.

    is_enabled : bool
        Engine participation flag.

    is_static : bool
        Static sprite flag.
    """

    sprite_id: int
    name: str
    tags: set[str]

    parent: Any | None

    position: Vec2
    anchor: Vec2
    dimensions: Vec2

    z_index: int
    render_order: int
    color_fg: Color
    color_bg: Color
    is_visible: bool
    is_flipped_x: bool
    is_flipped_y: bool
    render_cache: str
    is_dirty: bool

    animations: dict[str, Animation.Animation]
    current_animation_key: str
    animation_speed: float
    frame_index: int
    frame_interval: float
    last_frame_time: float
    is_looping: bool
    is_playing: bool

    hitbox: Rect

    is_enabled: bool
    is_static: bool

    def __init__(self) -> None:
        """
        Initialize a new Sprite instance.

        This sets up default values for all
        transform, rendering, animation, and
        engine state properties.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        ...

    def setColor(
            self,
            color_fg: Color | tuple[int, int, int] | None = ...,
            color_bg: Color | tuple[int, int, int] | None = ...
    ) -> None:
        """
        Set the foreground and background colors of the sprite.

        Parameters
        ----------
        color_fg : Color | tuple[int, int, int] | None, optional
            Foreground RGB color. Can be a Color instance or an (R, G, B) tuple.
            If None, the foreground color is unchanged.
        color_bg : Color | tuple[int, int, int] | None, optional
            Background RGB color. Can be a Color instance or an (R, G, B) tuple.
            If None, the background color is unchanged.

        Returns
        -------
        None
        """
        ...

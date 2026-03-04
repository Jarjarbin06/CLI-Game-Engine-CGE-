#############################
###                       ###
###          CGE          ###
###                       ###
###       STUB FILE       ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


## API STUB ##
class Vec2:
    """
    2D integer vector.

    Attributes
    ----------
    x : int
        Horizontal coordinate.
    y : int
        Vertical coordinate.
    """

    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a 2D vector.

        Parameters
        ----------
        x : int
            Horizontal coordinate.
        y : int
            Vertical coordinate.

        Returns
        -------
        None
        """
        ...


class Color:
    """
    RGB color container.

    Attributes
    ----------
    r : int
        Red channel (0–255).
    g : int
        Green channel (0–255).
    b : int
        Blue channel (0–255).
    """

    r: int
    g: int
    b: int

    def __init__(self, r: int, g: int, b: int) -> None:
        """
        Initialize an RGB color.

        Parameters
        ----------
        r : int
            Red channel (0–255).
        g : int
            Green channel (0–255).
        b : int
            Blue channel (0–255).

        Returns
        -------
        None
        """
        ...


class Rect:
    """
    Axis-aligned rectangle.

    Attributes
    ----------
    x : int
        Left position.
    y : int
        Top position.
    width : int
        Rectangle width.
    height : int
        Rectangle height.
    """

    x: int
    y: int
    width: int
    height: int

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """
        Initialize an axis-aligned rectangle.

        Parameters
        ----------
        x : int
            Left position.
        y : int
            Top position.
        width : int
            Rectangle width.
        height : int
            Rectangle height.

        Returns
        -------
        None
        """
        ...

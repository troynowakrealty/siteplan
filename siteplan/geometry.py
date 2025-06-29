from dataclasses import dataclass
from math import sqrt
from typing import Union, Tuple

@dataclass(frozen=True)
class Point:
    x: float = 0
    y: float = 0

@dataclass(frozen=True)
class Size:
    width: float = 0
    height: float = 0

class Rectangle:
    def __init__(self, *args):
        # Accept (x, y, width, height)
        if len(args) == 4 and all(isinstance(v, (int, float)) for v in args):
            x, y, w, h = args
            self.origin = Point(x, y)
            self.size = Size(w, h)
        # Accept (Point, Size)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Size):
            self.origin = args[0]
            self.size = args[1]
        else:
            raise TypeError("Rectangle requires (x, y, w, h) or (Point, Size)")

    @property
    def x(self):
        return self.origin.x

    @property
    def y(self):
        return self.origin.y

    @property
    def width(self):
        return self.size.width

    @property
    def height(self):
        return self.size.height

    def center(self) -> Point:
        return Point(
            self.x + self.width/2,
            self.y + self.height/2
        )

    def move(self, dx: float, dy: float) -> 'Rectangle':
        return Rectangle(
            self.x + dx,
            self.y + dy,
            self.width,
            self.height
        )

def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

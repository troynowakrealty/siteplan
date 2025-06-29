<<<<<<< HEAD
from dataclasses import dataclass


@dataclass
class Point:
    """A 2D point."""

    x: float
    y: float


@dataclass
class Size:
    """Width and height container."""

    width: float
    height: float
=======
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple
import math

Point = Tuple[float, float]


def distance(p1: Point, p2: Point) -> float:
    """Return Euclidean distance between two points."""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
>>>>>>> origin/main


@dataclass
class Rectangle:
<<<<<<< HEAD
    """Axis aligned rectangle."""

    origin: Point
    size: Size

    @property
    def x(self) -> float:
        return self.origin.x

    @property
    def y(self) -> float:
        return self.origin.y

    @property
    def width(self) -> float:
        return self.size.width

    @property
    def height(self) -> float:
        return self.size.height

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def bottom(self) -> float:
        return self.y + self.height

    def translate(self, dx: float, dy: float) -> "Rectangle":
        """Return a translated copy of the rectangle."""
        return Rectangle(Point(self.x + dx, self.y + dy), Size(self.width, self.height))

    def scale(self, factor: float) -> "Rectangle":
        """Return a uniformly scaled copy of the rectangle."""
        return Rectangle(
            Point(self.x * factor, self.y * factor),
            Size(self.width * factor, self.height * factor),
        )
=======
    x: float
    y: float
    width: float
    height: float

    def center(self) -> Point:
        return self.x + self.width / 2, self.y + self.height / 2

    def move(self, dx: float, dy: float) -> Rectangle:
        return Rectangle(self.x + dx, self.y + dy, self.width, self.height)
>>>>>>> origin/main

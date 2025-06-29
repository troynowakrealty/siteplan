from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple
import math

Point = Tuple[float, float]


def distance(p1: Point, p2: Point) -> float:
    """Return Euclidean distance between two points."""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


@dataclass
class Rectangle:
    x: float
    y: float
    width: float
    height: float

    def center(self) -> Point:
        return self.x + self.width / 2, self.y + self.height / 2

    def move(self, dx: float, dy: float) -> Rectangle:
        return Rectangle(self.x + dx, self.y + dy, self.width, self.height)

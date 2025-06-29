from dataclasses import dataclass
from math import sqrt

@dataclass(frozen=True)
class Point:
    x: float = 0
    y: float = 0

@dataclass(frozen=True)
class Size:
    width: float = 0
    height: float = 0

@dataclass(frozen=True)
class Rectangle:
    origin: Point
    size: Size

    def center(self) -> Point:
        return Point(
            self.origin.x + self.size.width / 2,
            self.origin.y + self.size.height / 2
        )

    def move(self, dx: float, dy: float) -> 'Rectangle':
        return Rectangle(
            origin=Point(self.origin.x + dx, self.origin.y + dy),
            size=self.size
        )

def distance(a: tuple, b: tuple) -> float:
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

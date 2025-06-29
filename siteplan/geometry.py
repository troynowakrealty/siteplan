from dataclasses import dataclass
from math import sqrt

@dataclass
class Point:
    x: float = 0
    y: float = 0

@dataclass
class Size:
    width: float = 0
    height: float = 0

@dataclass
class Rectangle:
    x: float
    y: float
    width: float
    height: float

    def center(self):
        return Point(self.x + self.width / 2, self.y + self.height / 2)

def distance(a: tuple, b: tuple) -> float:
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

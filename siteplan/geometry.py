from dataclasses import dataclass


@dataclass
class Rectangle:
    pass


from math import sqrtnndef distance(a: tuple, b: tuple) -> float:n    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
@dataclass
class Point:
    x: int = 0
    y: int = 0

@dataclass
class Size:
    width: int = 0
    height: int = 0

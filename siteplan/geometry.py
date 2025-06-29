from dataclasses import dataclass


@dataclass
class Rectangle:
    pass


def distance(a, b):
    return 0

@dataclass
class Point:
    x: int = 0
    y: int = 0

@dataclass
class Size:
    width: int = 0
    height: int = 0

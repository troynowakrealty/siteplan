from math import sqrt

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Size:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

class Rectangle:
    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Size):
            self.x = args[0].x
            self.y = args[0].y
            self.width = args[1].width
            self.height = args[1].height
        elif len(args) == 4:
            self.x, self.y, self.width, self.height = args
        else:
            raise ValueError("Invalid arguments for Rectangle constructor")

    def center(self):
        return (self.x + self.width / 2, self.y + self.height / 2)

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
    return self

def distance(a: tuple, b: tuple) -> float:
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

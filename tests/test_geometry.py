from siteplan.geometry import Rectangle, distance


def test_distance():
    assert distance((0, 0), (3, 4)) == 5


def test_rectangle_move_and_center():
    rect = Rectangle(0, 0, 10, 20)
    moved = rect.move(5, 5)
    assert moved.x == 5 and moved.y == 5
    assert moved.center() == (10, 15)

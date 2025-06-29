from siteplan.geometry import Point, Rectangle, Size
from siteplan.svg_writer import svg_footer, svg_header, svg_line, svg_polygon, svg_rect


def test_svg_rect():
    rect = Rectangle(Point(0, 0), Size(10, 5))
    tag = svg_rect(rect, fill="none")
    assert tag == "<rect x='0' y='0' width='10' height='5' fill='none' />"


def test_svg_line():
    p1 = Point(0, 0)
    p2 = Point(5, 5)
    tag = svg_line(p1, p2, stroke="black")
    assert tag == "<line x1='0' y1='0' x2='5' y2='5' stroke='black' />"


def test_svg_polygon():
    points = [Point(0, 0), Point(1, 0), Point(1, 1)]
    tag = svg_polygon(points, stroke="black", fill="none")
    assert tag == "<polygon points='0,0 1,0 1,1' stroke='black' fill='none' />"


def test_svg_header_footer():
    header = svg_header(100, 50)
    footer = svg_footer()
    assert (
        header.startswith("<svg")
        and "width='100'" in header
        and "height='50'" in header
    )
    assert footer == "</svg>"

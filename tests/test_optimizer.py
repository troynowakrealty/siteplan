from siteplan.geometry import Rectangle
from siteplan.layout import Layout
from siteplan.optimizer import separate_shapes


def test_separate_shapes():
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 100, 50))
    layout.add_shape(Rectangle(50, 25, 80, 40))
    separate_shapes(layout, min_dist=10)
    rect1, rect2 = layout.shapes
    assert rect2.x >= rect1.x + rect1.width + 10

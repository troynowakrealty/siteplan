from siteplan.geometry import Rectangle
from siteplan.layout import Layout
from siteplan.optimizer import apply_constraints, separate_shapes


def test_separate_shapes():
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 100, 50))
    layout.add_shape(Rectangle(50, 25, 80, 40))
    separate_shapes(layout, min_dist=10)
    rect1, rect2 = layout.shapes
    assert rect2.x >= rect1.x + rect1.width + 10


def test_apply_constraints():
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 40, 20))
    placements = [
        {
            "setbacks": {"left": 10, "bottom": 5, "right": 10, "top": 5},
            "facing": "east",
            "property_width": 100,
            "property_height": 60,
        }
    ]
    apply_constraints(layout, placements)
    rect = layout.shapes[0]
    # width/height swapped due to east facing
    assert rect.width == 20 and rect.height == 40
    # setbacks enforced on all sides
    assert rect.x >= 10
    assert rect.y >= 5
    assert rect.x + rect.width <= 100 - 10
    assert rect.y + rect.height <= 60 - 5

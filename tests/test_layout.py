from siteplan import layout


def test_generate_siteplan_rectangles():
    shapes = layout.generate_siteplan()
    assert isinstance(shapes, list)
    assert len(shapes) >= 4

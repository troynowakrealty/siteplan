import os

import geometry


def test_ft_to_px():
    assert geometry.ft_to_px(5) == 50


def test_rect_area():
    assert geometry.rect_area(3, 4) == 12


def test_rect_pixels():
    rect = geometry.rect_pixels((1, 2), 3, 4)
    assert rect == (10, 20, 30, 40)

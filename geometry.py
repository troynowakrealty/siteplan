SCALE = 10


def ft_to_px(feet: float) -> float:
    """Convert feet to pixels using SCALE."""
    return feet * SCALE


def rect_area(width_ft: float, height_ft: float) -> float:
    """Return area in square feet."""
    return width_ft * height_ft


def rect_pixels(origin_ft, width_ft: float, height_ft: float):
    """Return rectangle params in pixels (x, y, w, h)."""
    x_ft, y_ft = origin_ft
    return (
        ft_to_px(x_ft),
        ft_to_px(y_ft),
        ft_to_px(width_ft),
        ft_to_px(height_ft),
    )

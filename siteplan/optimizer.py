from __future__ import annotations

from .layout import Layout


def separate_shapes(layout: Layout, min_dist: float = 10) -> Layout:
    """Ensure shapes do not overlap by translating them if needed."""
    for i, rect in enumerate(layout.shapes):
        for other in layout.shapes[i + 1 :]:
            overlap_x = rect.x + rect.width + min_dist - other.x
            overlap_y = rect.y + rect.height + min_dist - other.y
            if overlap_x > 0 and overlap_y > 0:
                other.move(overlap_x, overlap_y)
    return layout

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


def apply_constraints(layout: Layout, placements: list[dict]) -> Layout:
    """Apply basic setback and orientation rules to shapes in *layout*.

    ``placements`` should be a list of dictionaries matching the order of
    ``layout.shapes``.  Each dictionary may contain:

    - ``setbacks``: mapping with ``left``, ``right``, ``top`` and ``bottom``
      setback distances. Missing values default to ``0``.
    - ``facing``: one of ``"north"``, ``"south"``, ``"east"`` or ``"west"`` to
      indicate orientation.  East/West swap the rectangle dimensions.
    - ``property_width`` and ``property_height``: optional dimensions of the
      property.  When provided, right and top setbacks are enforced against
      these bounds.
    """

    for rect, info in zip(layout.shapes, placements):
        setbacks = info.get("setbacks", {})
        left = setbacks.get("left", 0)
        right = setbacks.get("right", 0)
        top = setbacks.get("top", 0)
        bottom = setbacks.get("bottom", 0)

        # Apply rotation based on facing
        facing = str(info.get("facing", "")).lower()
        if facing in {"east", "west"}:
            rect.width, rect.height = rect.height, rect.width

        # Enforce left/bottom setbacks by shifting shape positively
        if rect.x < left:
            rect.x = left
        if rect.y < bottom:
            rect.y = bottom

        # Enforce right/top setbacks if property bounds are known
        prop_w = info.get("property_width")
        prop_h = info.get("property_height")
        if prop_w is not None and rect.x + rect.width > prop_w - right:
            rect.x = prop_w - right - rect.width
        if prop_h is not None and rect.y + rect.height > prop_h - top:
            rect.y = prop_h - top - rect.height

    return layout

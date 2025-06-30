from __future__ import annotations

from math import sqrt
from typing import Iterable, Mapping, Optional

from .geometry import Point, Rectangle


SVG_NS = "http://www.w3.org/2000/svg"


def _attrs_to_str(attrs: Mapping[str, object]) -> str:
    """Convert attribute dictionary to a string for tag construction."""
    return " ".join(f"{key}='{value}'" for key, value in attrs.items())


def svg_tag(name: str, self_close: bool = False, **attrs: object) -> str:
    """Generate a generic SVG tag."""
    attr_str = _attrs_to_str(attrs)
    if self_close:
        return f"<{name} {attr_str} />"
    return f"<{name} {attr_str}>"


def svg_close(name: str) -> str:
    """Return a closing tag for *name*."""
    return f"</{name}>"


def svg_rect(rect: Rectangle, **attrs: object) -> str:
    """Generate a ``<rect>`` element from ``Rectangle``."""
    rect_attrs = {
        "x": rect.x,
        "y": rect.y,
        "width": rect.width,
        "height": rect.height,
    }
    rect_attrs.update(attrs)
    return svg_tag("rect", self_close=True, **rect_attrs)


def svg_line(p1: Point, p2: Point, **attrs: object) -> str:
    """Generate a ``<line>`` element."""
    line_attrs = {"x1": p1.x, "y1": p1.y, "x2": p2.x, "y2": p2.y}
    line_attrs.update(attrs)
    return svg_tag("line", self_close=True, **line_attrs)


def svg_polygon(points: Iterable[Point], **attrs: object) -> str:
    """Generate a ``<polygon>`` element from a sequence of points."""
    point_str = " ".join(f"{p.x},{p.y}" for p in points)
    poly_attrs = {"points": point_str}
    poly_attrs.update(attrs)
    return svg_tag("polygon", self_close=True, **poly_attrs)


def svg_text(x: float, y: float, text: str, **attrs: object) -> str:
    """Generate a ``<text>`` element."""
    text_attrs = {"x": x, "y": y}
    text_attrs.update(attrs)
    attr_str = _attrs_to_str(text_attrs)
    return f"<text {attr_str}>{text}</text>"


def svg_property_boundary(rect: Rectangle, **attrs: object) -> str:
    """Draw a dashed rectangle to indicate the property boundary."""
    boundary_attrs = {
        "fill": "none",
        "stroke": "black",
        "stroke-dasharray": "4",
    }
    boundary_attrs.update(attrs)
    return svg_rect(rect, **boundary_attrs)


def _arrowhead(tip: Point, tail: Point, size: float) -> list[Point]:
    """Calculate points for an arrow head polygon."""
    dx = tail.x - tip.x
    dy = tail.y - tip.y
    length = sqrt(dx * dx + dy * dy) or 1
    ux = dx / length
    uy = dy / length
    left = Point(
        tip.x + ux * size - uy * (size / 2), tip.y + uy * size + ux * (size / 2)
    )
    right = Point(
        tip.x + ux * size + uy * (size / 2), tip.y + uy * size - ux * (size / 2)
    )
    return [tip, left, right]


def svg_arrow(p1: Point, p2: Point, size: float = 10, **attrs: object) -> str:
    """Draw a line with an arrow head pointing to ``p2``."""
    line = svg_line(p1, p2, **attrs)
    head = svg_polygon(_arrowhead(p2, p1, size), **attrs)
    return line + "\n" + head


def svg_dimension_callout(
    p1: Point,
    p2: Point,
    text: str,
    *,
    size: float = 10,
    text_style: Optional[Mapping[str, object]] = None,
    **attrs: object,
) -> str:
    """Draw a dimension line with arrowheads at both ends and a centered label."""
    pieces = [svg_line(p1, p2, **attrs)]
    pieces.append(svg_polygon(_arrowhead(p1, p2, size), **attrs))
    pieces.append(svg_polygon(_arrowhead(p2, p1, size), **attrs))
    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2
    text_attrs = {"fill": attrs.get("stroke", "black")}
    if text_style:
        text_attrs.update(text_style)
    pieces.append(svg_text(mid_x, mid_y - size, text, **text_attrs))
    return "\n".join(pieces)


def svg_grid(width: float, height: float, spacing: float = 100) -> str:
    """Generate light gridlines for the plan."""
    lines = []
    x = 0
    while x <= width:
        lines.append(svg_line(Point(x, 0), Point(x, height), stroke="#ddd"))
        x += spacing
    y = 0
    while y <= height:
        lines.append(svg_line(Point(0, y), Point(width, y), stroke="#ddd"))
        y += spacing
    return "\n".join(lines)


def svg_header(width: float, height: float, **attrs: object) -> str:
    """Return the opening ``<svg>`` tag with namespace and size."""
    header_attrs = {"xmlns": SVG_NS, "width": width, "height": height}
    header_attrs.update(attrs)
    return svg_tag("svg", **header_attrs)


def svg_footer() -> str:
    """Return closing ``</svg>`` tag."""
    return svg_close("svg")

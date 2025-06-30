from __future__ import annotations

from typing import Iterable, Mapping

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

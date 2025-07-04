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


def svg_boundary(rect: Rectangle, offset: float = 5, **attrs: object) -> str:
    """Generate a dashed boundary polygon around *rect*."""
    points = [
        Point(rect.x - offset, rect.y - offset),
        Point(rect.x + rect.width + offset, rect.y - offset),
        Point(rect.x + rect.width + offset, rect.y + rect.height + offset),
        Point(rect.x - offset, rect.y + rect.height + offset),
    ]
    boundary_attrs = {"fill": "none", "stroke": "red", "stroke-dasharray": "4 2"}
    boundary_attrs.update(attrs)
    return svg_polygon(points, **boundary_attrs)


def svg_dimensions(rect: Rectangle, scale: float = 10, font_size: int = 12) -> str:
    """Return simple width/height dimension lines and labels for *rect*."""
    elements = []
    top_y = rect.y - 10
    left_x = rect.x - 10
    # dimension lines
    elements.append(
        svg_line(
            Point(rect.x, top_y), Point(rect.x + rect.width, top_y), stroke="black"
        )
    )
    elements.append(
        svg_line(
            Point(left_x, rect.y), Point(left_x, rect.y + rect.height), stroke="black"
        )
    )
    # labels
    elements.append(
        svg_text(
            rect.x + rect.width / 2,
            top_y - 2,
            f"{rect.width/scale} ft",
            fill="black",
            **{"text-anchor": "middle", "font-size": font_size},
        )
    )
    elements.append(
        svg_text(
            left_x - 2,
            rect.y + rect.height / 2,
            f"{rect.height/scale} ft",
            fill="black",
            transform=f"rotate(-90 {left_x - 2},{rect.y + rect.height / 2})",
            **{"text-anchor": "middle", "font-size": font_size},
        )
    )
    return "\n".join(elements)


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

def write_svg(shapes, output_path):
    """Render a list of (label, Rectangle) and save as an SVG file."""
    width = 2 * 46  # 2 lots wide
    height = 124    # max lot depth

    with open(output_path, 'w') as f:
        f.write(svg_header(width=width, height=height, viewBox=f"0 0 {width} {height}") + "\n")
        for label, rect in shapes:
            f.write(svg_rect(rect, fill="none", stroke="black") + "\n")
            label_x = rect.x + 1
            label_y = rect.y + 3
            f.write(f"<text x='{label_x}' y='{label_y}' font-size='2'>{label}</text>\n")
        f.write(svg_footer() + "\n")

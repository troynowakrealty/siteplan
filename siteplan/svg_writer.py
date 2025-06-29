from pathlib import Path
from typing import Iterable
import xml.etree.ElementTree as ET

from .layout import Rect


def write_svg(shapes: Iterable[Rect], path: Path, scale: float = 10.0) -> None:
    """Write shapes to an SVG file at the given path."""
    path = Path(path)
    width = max(r.x + r.width for r in shapes) * scale
    height = max(r.y + r.height for r in shapes) * scale

    root = ET.Element(
        "svg",
        xmlns="http://www.w3.org/2000/svg",
        width=str(width),
        height=str(height),
    )

    for rect in shapes:
        ET.SubElement(
            root,
            "rect",
            {
                "x": str(rect.x * scale),
                "y": str(rect.y * scale),
                "width": str(rect.width * scale),
                "height": str(rect.height * scale),
                "fill": rect.fill,
                "stroke": rect.stroke,
            },
        )

    tree = ET.ElementTree(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        tree.write(f)

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from pathlib import Path

from .geometry import Rectangle


@dataclass
class Layout:
    shapes: List[Rectangle] = field(default_factory=list)

    def add_shape(self, shape: Rectangle) -> None:
        self.shapes.append(shape)

    def export_svg(self, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            f.write('<svg xmlns="http://www.w3.org/2000/svg">\n')
            for rect in self.shapes:
                f.write(
                    f'  <rect x="{rect.x}" y="{rect.y}" '
                    f'width="{rect.width}" height="{rect.height}" '
                    'fill="none" stroke="black"/>\n'
                )
            f.write("</svg>\n")

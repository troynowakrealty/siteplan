from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from pathlib import Path

from .geometry import Rectangle
from .svg_writer import svg_footer, svg_grid, svg_header, svg_rect, svg_text


@dataclass
class Layout:
    shapes: List[Rectangle] = field(default_factory=list)

    def add_shape(self, shape: Rectangle) -> None:
        self.shapes.append(shape)

    def export_svg(self, path: Path, scale: float = 10) -> None:
        """Export layout as scaled SVG with gridlines and basic dimensions."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        max_x = max((r.x + r.width for r in self.shapes), default=0)
        max_y = max((r.y + r.height for r in self.shapes), default=0)

        width = max_x + 20
        height = max_y + 20

        with path.open("w", encoding="utf-8") as f:
            f.write(svg_header(width, height) + "\n")
            f.write(svg_grid(width, height) + "\n")
            for rect in self.shapes:
                f.write(svg_rect(rect, fill="none", stroke="black") + "\n")
                label_x = rect.x + rect.width / 2
                label_y = rect.y - 5
                dims = f"{rect.width/scale}x{rect.height/scale} ft"
                f.write(
                    svg_text(
                        label_x,
                        label_y,
                        dims,
                        fill="black",
                        **{"text-anchor": "middle", "font-size": 12},
                    )
                    + "\n"
                )
            f.write(svg_footer() + "\n")

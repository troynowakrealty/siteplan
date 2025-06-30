from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Mapping, Optional
from pathlib import Path
import json
import pickle

from .geometry import Point, Rectangle
from .svg_writer import (
    svg_dimension_callout,
    svg_footer,
    svg_grid,
    svg_header,
    svg_property_boundary,
    svg_rect,
    svg_text,
)


@dataclass
class Layout:
    shapes: List[Rectangle] = field(default_factory=list)

    def add_shape(self, shape: Rectangle) -> None:
        self.shapes.append(shape)

    def export_svg(
        self,
        path: Path,
        *,
        scale: float = 10,
        show_grid: bool = True,
        arrow_size: float = 10,
        text_style: Optional[Mapping[str, object]] = None,
    ) -> None:
        """Export layout as scaled SVG with gridlines and dimension callouts."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        max_x = max((r.x + r.width for r in self.shapes), default=0)
        max_y = max((r.y + r.height for r in self.shapes), default=0)

        width = max_x + 20
        height = max_y + 20

        with path.open("w", encoding="utf-8") as f:
            f.write(svg_header(width, height) + "\n")
            if show_grid:
                f.write(svg_grid(width, height) + "\n")

            boundary = Rectangle(0, 0, max_x, max_y)
            f.write(svg_property_boundary(boundary) + "\n")

            text_style = text_style or {"font-size": 12, "text-anchor": "middle"}

            for rect in self.shapes:
                f.write(svg_rect(rect, fill="none", stroke="black") + "\n")

                width_text = f"{rect.width/scale} ft"
                start = Point(rect.x, rect.y - arrow_size * 2)
                end = Point(rect.x + rect.width, rect.y - arrow_size * 2)
                f.write(
                    svg_dimension_callout(
                        start,
                        end,
                        width_text,
                        size=arrow_size,
                        text_style=text_style,
                        stroke="black",
                    )
                    + "\n"
                )

                height_text = f"{rect.height/scale} ft"
                start_h = Point(rect.x - arrow_size * 2, rect.y)
                end_h = Point(rect.x - arrow_size * 2, rect.y + rect.height)
                f.write(
                    svg_dimension_callout(
                        start_h,
                        end_h,
                        height_text,
                        size=arrow_size,
                        text_style=text_style,
                        stroke="black",
                    )
                    + "\n"
                )

            f.write(svg_footer() + "\n")

    def save(self, path: Path) -> None:
        path = Path(path)
        if path.suffix == ".json":
            data = {"shapes": [[r.x, r.y, r.width, r.height] for r in self.shapes]}
            path.write_text(json.dumps(data))
        else:
            with path.open("wb") as f:
                pickle.dump(self, f)

    @classmethod
    def load(cls, path: Path) -> "Layout":
        path = Path(path)
        if path.suffix == ".json":
            data = json.loads(path.read_text())
            layout = cls()
            for vals in data.get("shapes", []):
                layout.add_shape(Rectangle(*vals))
            return layout
        else:
            with path.open("rb") as f:
                return pickle.load(f)

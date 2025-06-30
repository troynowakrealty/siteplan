from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from pathlib import Path
import json
import pickle

from .geometry import Rectangle
from .svg_writer import (
    svg_boundary,
    svg_dimensions,
    svg_footer,
    svg_grid,
    svg_header,
    svg_rect,
)


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
                f.write(svg_boundary(rect) + "\n")
                f.write(svg_dimensions(rect, scale) + "\n")
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

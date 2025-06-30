from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from siteplan.geometry import Rectangle
from siteplan.layout import Layout
from siteplan.optimizer import separate_shapes

PROMPT = """
setback 5
place duplex 40x30 at 0,0 orientation east
place adu 20x20 at 50,0 orientation south
"""


def parse_multi_prompt(text: str) -> Tuple[List[Rectangle], float]:
    """Parse instructions with orientation and setbacks."""
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    shapes: List[Rectangle] = []
    setback = 0.0
    for line in lines:
        parts = line.lower().split()
        if parts[0] == "setback":
            setback = float(parts[1])
            continue
        if parts[0] != "place" or "at" not in parts:
            raise ValueError(f"Invalid instruction: {line}")
        idx_at = parts.index("at")
        dims = parts[2].split("x")
        width_ft, height_ft = map(float, dims)
        x_ft, y_ft = map(float, parts[idx_at + 1].split(","))
        orientation = "east"
        if "orientation" in parts:
            orientation = parts[parts.index("orientation") + 1]
        if orientation in {"north", "south"}:
            width_ft, height_ft = height_ft, width_ft
        rect = Rectangle(x_ft * 10, y_ft * 10, width_ft * 10, height_ft * 10)
        shapes.append(rect)
    return shapes, setback


def main() -> None:
    rects, setback = parse_multi_prompt(PROMPT)
    layout = Layout()
    for rect in rects:
        layout.add_shape(rect)
    if setback:
        separate_shapes(layout, min_dist=setback * 10)
    layout.export_svg(Path("output/examples/duplex_adu.svg"))


if __name__ == "__main__":
    main()

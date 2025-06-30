from __future__ import annotations

from typing import List

from .geometry import Rectangle


def parse_prompt(text: str) -> List[Rectangle]:
    """Parse a structured prompt and return rectangles scaled 1ft = 10px."""
    shapes: List[Rectangle] = []
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    for line in lines:
        parts = line.split()
        if len(parts) != 5 or parts[0].lower() != "place" or parts[3].lower() != "at":
            raise ValueError(f"Invalid instruction: {line}")
        dims = parts[2].lower().split("x")
        if len(dims) != 2:
            raise ValueError(f"Invalid dimensions in: {line}")
        width_ft, height_ft = map(float, dims)
        x_ft, y_ft = map(float, parts[4].split(","))
        rect = Rectangle(x_ft * 10, y_ft * 10, width_ft * 10, height_ft * 10)
        shapes.append(rect)
    return shapes

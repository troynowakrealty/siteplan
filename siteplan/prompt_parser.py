from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .geometry import Rectangle


@dataclass
class Placement:
    """Rectangle placement details parsed from a prompt line."""

    rect: Rectangle
    facing: Optional[str] = None
    setbacks: Dict[str, float] = field(default_factory=dict)


def parse_prompt(text: str) -> List[Placement]:
    """Parse a structured prompt and return rectangle placements."""

    placements: List[Placement] = []
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    for line in lines:
        parts = line.split()
        if parts[0].lower() != "place" or "at" not in parts:
            raise ValueError(f"Invalid instruction: {line}")

        try:
            at_idx = parts.index("at")
        except ValueError as exc:  # pragma: no cover - safeguard
            raise ValueError(f"Invalid instruction: {line}") from exc

        if at_idx != 3 or len(parts) < 5:
            raise ValueError(f"Invalid instruction: {line}")

        dims = parts[2].lower().split("x")
        if len(dims) != 2:
            raise ValueError(f"Invalid dimensions in: {line}")

        width_ft, height_ft = map(float, dims)
        x_ft, y_ft = map(float, parts[at_idx + 1].split(","))

        facing: Optional[str] = None
        setbacks: Dict[str, float] = {}

        i = at_idx + 2
        while i < len(parts):
            token = parts[i].lower()
            if token == "facing":
                if i + 1 >= len(parts):
                    raise ValueError(f"Missing direction after 'facing' in: {line}")
                facing = parts[i + 1].lower()
                i += 2
            elif token in {"n", "s", "e", "w"}:
                if i + 2 >= len(parts) or parts[i + 1].lower() != "setback":
                    raise ValueError(f"Invalid setback syntax in: {line}")
                setbacks[token] = float(parts[i + 2])
                i += 3
            else:
                raise ValueError(f"Unknown token '{parts[i]}' in: {line}")

        rect = Rectangle(x_ft * 10, y_ft * 10, width_ft * 10, height_ft * 10)
        placements.append(Placement(rect, facing, setbacks))

    return placements

from dataclasses import dataclass
from typing import List


@dataclass
class Rect:
    """Represents a rectangle in feet."""

    x: float
    y: float
    width: float
    height: float
    fill: str = "none"
    stroke: str = "black"


def generate_siteplan() -> List[Rect]:
    """Return rectangles representing a simple duplex and ADU site plan."""
    shapes: List[Rect] = []

    # Lot dimensions (feet)
    lot_width, lot_height = 50.0, 100.0
    shapes.append(Rect(0, 0, lot_width, lot_height, fill="lightgreen"))

    # Duplex units
    duplex_width, duplex_height = 20.0, 40.0
    padding = 5.0
    shapes.append(Rect(padding, padding, duplex_width, duplex_height, fill="gray"))
    shapes.append(
        Rect(
            padding,
            lot_height - duplex_height - padding,
            duplex_width,
            duplex_height,
            fill="gray",
        )
    )

    # Accessory Dwelling Unit (ADU)
    adu_width, adu_height = 15.0, 20.0
    shapes.append(
        Rect(
            lot_width - adu_width - padding,
            (lot_height - adu_height) / 2,
            adu_width,
            adu_height,
            fill="brown",
        )
    )

    return shapes

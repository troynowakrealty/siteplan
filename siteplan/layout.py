from __future__ import annotations

from dataclasses import dataclass
from typing import List

SCALE = 10  # pixels per foot


@dataclass
class Rectangle:
    """Simple rectangle geometry in feet."""

    x: float
    y: float
    width: float
    height: float

    def to_pixels(self) -> "Rectangle":
        """Return a rectangle scaled to pixels."""
        return Rectangle(
            x=self.x * SCALE,
            y=self.y * SCALE,
            width=self.width * SCALE,
            height=self.height * SCALE,
        )


@dataclass
class LotSpec:
    width: float
    depth: float
    front_setback: float
    rear_setback: float
    side_setback: float


@dataclass
class BuildingSpec:
    width: float
    depth: float


@dataclass
class Layout:
    lot: Rectangle
    duplex: Rectangle
    adu: Rectangle
    parking: List[Rectangle]

    def to_pixels(self) -> "Layout":
        return Layout(
            lot=self.lot.to_pixels(),
            duplex=self.duplex.to_pixels(),
            adu=self.adu.to_pixels(),
            parking=[p.to_pixels() for p in self.parking],
        )


def compute_layout(
    lot: LotSpec, duplex: BuildingSpec, adu: BuildingSpec, parking_depth: float = 20
) -> Layout:
    """Compute placement for duplex, ADU, and parking within a lot.

    Parameters
    ----------
    lot: LotSpec
        Dimensions of the lot and setbacks in feet.
    duplex: BuildingSpec
        Size of the duplex building in feet.
    adu: BuildingSpec
        Size of the ADU in feet.
    parking_depth: float
        Depth of the parking pad in feet.
    """
    lot_rect = Rectangle(0, 0, lot.width, lot.depth)

    duplex_x = lot.side_setback
    duplex_y = lot.front_setback
    duplex_rect = Rectangle(duplex_x, duplex_y, duplex.width, duplex.depth)

    adu_x = lot.width - lot.side_setback - adu.width
    adu_y = lot.depth - lot.rear_setback - adu.depth
    adu_rect = Rectangle(adu_x, adu_y, adu.width, adu.depth)

    parking_width = duplex.width / 2
    parking1 = Rectangle(
        duplex_x, duplex_y - parking_depth, parking_width, parking_depth
    )
    parking2 = Rectangle(
        duplex_x + parking_width, duplex_y - parking_depth, parking_width, parking_depth
    )

    return Layout(lot_rect, duplex_rect, adu_rect, [parking1, parking2])

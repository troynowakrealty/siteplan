from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from .geometry import Point, Rectangle
from .svg_writer import (
    svg_boundary,
    svg_dimensions,
    svg_footer,
    svg_header,
    svg_line,
    svg_polygon,
    svg_rect,
    svg_text,
)

SCALE = 10
LOT_WIDTH = 46
LOT_DEPTH = 124
FRONT_SETBACK = 18
REAR_SETBACK = 22
LEFT_SETBACK = 8
RIGHT_SETBACK = 5

FRONT_BUILDING_SIZE = (33, 28)
REAR_BUILDING_SIZE = (30, 20)
PARKING_SIZE = (9, 20)
TRASH_SIZE = (6, 20)

OUTPUT_PATH = Path("output/siteplan_dual_lot.svg")


Shape = Tuple[str, Rectangle]


def build_lot(x_offset_ft: float, left_sb: float, right_sb: float) -> List[Shape]:
    """Return shapes for a single lot starting at *x_offset_ft*."""
    x_offset = x_offset_ft * SCALE
    lot_w = LOT_WIDTH * SCALE
    lot_h = LOT_DEPTH * SCALE

    shapes: List[Shape] = []

    # Lot boundary
    lot = Rectangle(x_offset, 0, lot_w, lot_h)
    shapes.append(("Lot", lot))

    # Setback areas (optional shading)
    shapes.append(
        ("Front Setback", Rectangle(x_offset, 0, lot_w, FRONT_SETBACK * SCALE))
    )
    rear_rect = Rectangle(
        x_offset,
        lot_h - REAR_SETBACK * SCALE,
        lot_w,
        REAR_SETBACK * SCALE,
    )
    shapes.append(("Rear Setback", rear_rect))
    shapes.append(("Left Setback", Rectangle(x_offset, 0, left_sb * SCALE, lot_h)))
    right_rect = Rectangle(
        x_offset + lot_w - right_sb * SCALE,
        0,
        right_sb * SCALE,
        lot_h,
    )
    shapes.append(("Right Setback", right_rect))

    # Front building
    front_x = x_offset + (LOT_WIDTH - FRONT_BUILDING_SIZE[0]) / 2 * SCALE
    front_y = FRONT_SETBACK * SCALE
    front_unit = Rectangle(
        front_x,
        front_y,
        FRONT_BUILDING_SIZE[0] * SCALE,
        FRONT_BUILDING_SIZE[1] * SCALE,
    )
    shapes.append(("Front Unit", front_unit))

    # Rear building (Garage/ADU)
    adu_x = x_offset + (LOT_WIDTH - REAR_BUILDING_SIZE[0]) / 2 * SCALE
    adu_y = lot_h - REAR_SETBACK * SCALE - REAR_BUILDING_SIZE[1] * SCALE
    adu = Rectangle(
        adu_x,
        adu_y,
        REAR_BUILDING_SIZE[0] * SCALE,
        REAR_BUILDING_SIZE[1] * SCALE,
    )
    shapes.append(("Garage/ADU", adu))

    # Parking and trash behind ADU, centered
    row_w = 3 * PARKING_SIZE[0] + TRASH_SIZE[0]
    row_x = x_offset + (LOT_WIDTH - row_w) / 2 * SCALE
    parking_y = lot_h - PARKING_SIZE[1] * SCALE
    for i in range(3):
        px = row_x + i * PARKING_SIZE[0] * SCALE
        rect = Rectangle(
            px,
            parking_y,
            PARKING_SIZE[0] * SCALE,
            PARKING_SIZE[1] * SCALE,
        )
        shapes.append((f"Parking {i + 1}", rect))

    trash_x = row_x + 3 * PARKING_SIZE[0] * SCALE
    trash = Rectangle(
        trash_x,
        parking_y,
        TRASH_SIZE[0] * SCALE,
        TRASH_SIZE[1] * SCALE,
    )
    shapes.append(("Trash Pad", trash))

    return shapes


def generate_shapes() -> List[Shape]:
    shapes = []
    # Lot 1 on the left: right setback 5, left 8
    shapes.extend(build_lot(0, LEFT_SETBACK, RIGHT_SETBACK))
    # Lot 2 on the right: mirrored setbacks
    shapes.extend(build_lot(LOT_WIDTH, RIGHT_SETBACK, LEFT_SETBACK))
    return shapes


def write_svg(shapes: List[Shape], path: Path) -> None:
    width = LOT_WIDTH * 2 * SCALE
    height = LOT_DEPTH * SCALE
    lines = [svg_header(width, height, viewBox=f"0 0 {width} {height}")]

    for label, rect in shapes:
        style = {}
        if "Setback" in label:
            style = {"fill": "#cccccc", "fill-opacity": "0.2", "stroke": "none"}
        else:
            style = {"fill": "none", "stroke": "black"}
        lines.append(svg_rect(rect, **style))
        skip_labels = {
            "Lot",
            "Left Setback",
            "Right Setback",
            "Front Setback",
            "Rear Setback",
        }
        if label not in skip_labels:
            lines.append(
                svg_text(
                    rect.x + rect.width / 2,
                    rect.y + rect.height / 2,
                    label,
                    **{"text-anchor": "middle", "font-size": 12},
                )
            )
        if label == "Lot":
            lines.append(
                svg_rect(rect, fill="none", stroke="black", **{"stroke-width": 2})
            )
        lines.append(svg_boundary(rect))
        lines.append(svg_dimensions(rect, scale=SCALE))

    # North arrow
    arrow_y = 10
    arrow_x = width - 20
    lines.append(
        svg_text(
            arrow_x,
            arrow_y,
            "N",
            **{"font-size": 14, "text-anchor": "middle"},
        )
    )
    lines.append(
        svg_line(
            Point(arrow_x, arrow_y + 2),
            Point(arrow_x, arrow_y + 12),
            stroke="black",
        )
    )
    lines.append(
        svg_polygon(
            [
                Point(arrow_x - 3, arrow_y + 4),
                Point(arrow_x + 3, arrow_y + 4),
                Point(arrow_x, arrow_y),
            ],
            fill="black",
        )
    )

    lines.append(svg_footer())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines))


def main() -> List[Shape]:
    shapes = generate_shapes()
    write_svg(shapes, OUTPUT_PATH)
    return shapes


if __name__ == "__main__":
    main()

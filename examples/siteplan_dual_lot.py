from __future__ import annotations

from pathlib import Path

from siteplan.geometry import Point, Rectangle
from siteplan.svg_writer import svg_footer, svg_header, svg_line, svg_polygon, svg_rect

SCALE = 10


def main() -> None:
    width = 917.6
    height = 1102.2
    center_x = 467.6

    front_y = 18 * SCALE
    rear_y = 991.2

    lot2_left = 8 * SCALE
    lot2_right = center_x - 5 * SCALE
    lot1_left = center_x + 5 * SCALE
    lot1_right = width - 5 * SCALE

    out = Path("output/siteplan_dual_lot.svg")
    out.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(svg_header(width, height))

    # Lot rectangles
    lines.append(
        svg_rect(
            Rectangle(0, 0, 467.6, 1102.2),
            fill="none",
            stroke="black",
            **{"stroke-width": 2},
        )
    )
    lines.append(
        svg_rect(
            Rectangle(center_x, 0, 450.0, 1101.1),
            fill="none",
            stroke="black",
            **{"stroke-width": 2},
        )
    )

    # Center divider
    lines.append(svg_line(Point(center_x, 0), Point(center_x, height), stroke="black"))

    # Setback lines
    for x1, x2 in ((0, center_x), (center_x, width)):
        lines.append(
            svg_line(
                Point(x1, front_y),
                Point(x2, front_y),
                stroke="blue",
                **{"stroke-dasharray": "5,5"},
            )
        )
        lines.append(
            svg_line(
                Point(x1, rear_y),
                Point(x2, rear_y),
                stroke="blue",
                **{"stroke-dasharray": "5,5"},
            )
        )

    lines.append(
        svg_line(
            Point(lot2_left, 0),
            Point(lot2_left, 1102.2),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        svg_line(
            Point(lot2_right, 0),
            Point(lot2_right, 1102.2),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        svg_line(
            Point(lot1_left, 0),
            Point(lot1_left, 1101.1),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        svg_line(
            Point(lot1_right, 0),
            Point(lot1_right, 1101.1),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )

    # Duplexes
    duplex_w = 33 * SCALE
    duplex_h = 28 * SCALE
    lines.append(
        svg_rect(
            Rectangle(87.8, front_y, duplex_w, duplex_h), fill="blue", stroke="black"
        )
    )
    lines.append(
        svg_rect(
            Rectangle(517.6, front_y, duplex_w, duplex_h), fill="blue", stroke="black"
        )
    )

    # Porches
    porch_w = 6 * SCALE
    porch_h = 10 * SCALE
    porch_y = 120
    for x in (67.8, 237.8, 502.6, 672.6):
        lines.append(
            svg_rect(
                Rectangle(x, porch_y, porch_w, porch_h), fill="blue", stroke="black"
            )
        )

    # Garages with ADUs
    adu_w = 30 * SCALE
    adu_h = 20 * SCALE
    adu_y = 660
    lines.append(
        svg_rect(Rectangle(93.8, adu_y, adu_w, adu_h), fill="green", stroke="black")
    )
    lines.append(
        svg_rect(Rectangle(518.8, adu_y, adu_w, adu_h), fill="green", stroke="black")
    )

    # A/C units
    ac_size = 30
    for adu_x in (93.8, 518.8):
        lines.append(
            svg_rect(
                Rectangle(adu_x + adu_w + 10, adu_y + 20, ac_size, ac_size),
                fill="gray",
                stroke="black",
            )
        )

    # Stairs
    for adu_x in (93.8, 518.8):
        base_x = adu_x + adu_w / 2
        base_y = adu_y + adu_h
        lines.append(
            svg_line(Point(base_x, base_y), Point(base_x, base_y + 20), stroke="black")
        )
        lines.append(
            svg_polygon(
                [
                    Point(base_x - 5, base_y + 20),
                    Point(base_x + 5, base_y + 20),
                    Point(base_x, base_y + 30),
                ],
                fill="black",
            )
        )

    # Parking pads
    pad_w = 9 * SCALE
    pad_h = 20 * SCALE
    pad_y = 860
    for x in (93.8, 193.8, 293.8, 518.8, 618.8, 718.8):
        lines.append(
            svg_rect(Rectangle(x, pad_y, pad_w, pad_h), fill="yellow", stroke="black")
        )

    # Trash pads
    trash_w = 6 * SCALE
    trash_h = 20 * SCALE
    trash_y = 860
    lines.append(
        svg_rect(
            Rectangle(390, trash_y, trash_w, trash_h), fill="brown", stroke="black"
        )
    )
    lines.append(
        svg_rect(
            Rectangle(880, trash_y, trash_w, trash_h), fill="brown", stroke="black"
        )
    )

    lines.append(svg_footer())
    out.write_text("\n".join(lines))


if __name__ == "__main__":
    main()

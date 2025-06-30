from __future__ import annotations

from pathlib import Path

from siteplan.geometry import Point, Rectangle
from siteplan.svg_writer import svg_footer, svg_header, svg_line, svg_rect, svg_text

SCALE = 10


def main() -> None:
    width = 45 * SCALE
    height = 110.11 * SCALE

    front_y = 18 * SCALE
    rear_y = height - 11 * SCALE
    left_x = 8 * SCALE
    right_x = width - 5 * SCALE

    duplex_w = 33 * SCALE
    duplex_h = 28 * SCALE
    duplex_x = left_x
    duplex_y = front_y

    adu_w = 30 * SCALE
    adu_h = 20 * SCALE
    adu_x = left_x
    adu_y = duplex_y + duplex_h + 20 * SCALE

    parking_w = 9 * SCALE
    parking_h = 20 * SCALE
    parking_y = adu_y + adu_h

    trash_w = 60
    trash_h = parking_h
    trash_x = width - trash_w
    out = Path("output/siteplan_lot1.svg")
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append(svg_header(width, height))
    lines.append("  <!-- Lot 1 -->")
    lines.append(
        "  " + svg_rect(Rectangle(0, 0, width, height), fill="none", stroke="black")
    )
    lines.append(
        "  "
        + svg_text(width / 2, 20, "Lot 1", **{"text-anchor": "middle", "font-size": 14})
    )

    lines.append("")
    lines.append("  <!-- Setback lines -->")
    lines.append(
        "  "
        + svg_line(
            Point(0, front_y),
            Point(width, front_y),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  " + svg_text(5, front_y - 5, "Front setback 18'", **{"font-size": 12})
    )

    lines.append(
        "  "
        + svg_line(
            Point(0, rear_y),
            Point(width, rear_y),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  " + svg_text(5, rear_y - 6, "Rear setback 11'", **{"font-size": 12})
    )

    lines.append(
        "  "
        + svg_line(
            Point(left_x, 0),
            Point(left_x, height),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            left_x + 5,
            height / 2,
            "Left setback 8'",
            **{"font-size": 12},
            transform=f"rotate(-90 {left_x + 5},{height / 2})",
        )
    )

    lines.append(
        "  "
        + svg_line(
            Point(right_x, 0),
            Point(right_x, height),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            right_x - 5,
            height / 2,
            "Right setback 5'",
            **{"font-size": 12},
            transform=f"rotate(-90 {right_x - 5},{height / 2})",
        )
    )

    lines.append("")
    lines.append("  <!-- Duplex -->")
    lines.append(
        "  "
        + svg_rect(
            Rectangle(duplex_x, duplex_y, duplex_w, duplex_h),
            fill="#dddddd",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            duplex_x + duplex_w / 2,
            duplex_y + duplex_h / 2,
            "Duplex",
            **{"text-anchor": "middle", "font-size": 14},
        )
    )

    lines.append("")
    lines.append("  <!-- ADU -->")
    lines.append(
        "  "
        + svg_rect(
            Rectangle(adu_x, adu_y, adu_w, adu_h), fill="#cccccc", stroke="black"
        )
    )
    lines.append(
        "  "
        + svg_text(
            adu_x + adu_w / 2,
            adu_y + adu_h / 2,
            "ADU",
            **{"text-anchor": "middle", "font-size": 14},
        )
    )

    lines.append("")
    lines.append("  <!-- Parking Pads -->")
    lines.append(
        "  "
        + svg_rect(
            Rectangle(duplex_x, parking_y, parking_w, parking_h),
            fill="#eeeeee",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            duplex_x + parking_w / 2,
            parking_y + parking_h / 2,
            "Parking 1",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_rect(
            Rectangle(duplex_x + parking_w, parking_y, parking_w, parking_h),
            fill="#eeeeee",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            duplex_x + parking_w * 1.5,
            parking_y + parking_h / 2,
            "Parking 2",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_rect(
            Rectangle(duplex_x + parking_w * 2, parking_y, parking_w, parking_h),
            fill="#eeeeee",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            duplex_x + parking_w * 2.5,
            parking_y + parking_h / 2,
            "Parking 3",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )

    lines.append("")
    lines.append("  <!-- Trash Pad -->")
    lines.append(
        "  "
        + svg_rect(
            Rectangle(trash_x, parking_y, trash_w, trash_h),
            fill="#eeeeee",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            trash_x + trash_w / 2,
            parking_y + trash_h / 2,
            "Trash",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )

    lines.append(
        "  "
        + svg_text(
            width - 5,
            height - 5,
            "Scale 1\" = 10'",
            **{"text-anchor": "end", "font-size": 12},
        )
    )

    lines.append(svg_footer())
    out.write_text("\n".join(lines))


if __name__ == "__main__":
    main()

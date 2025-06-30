from __future__ import annotations

from pathlib import Path

from siteplan.geometry import Point, Rectangle
from siteplan.svg_writer import svg_footer, svg_header, svg_line, svg_rect, svg_text

SCALE = 10


def main() -> None:
    width = 917.6
    height = 1102.2
    center_x = 467.6
    lot2_height = 1102.2
    lot1_height = 1101.1

    front_y = 18 * SCALE
    rear_y = 991.2

    lot2_left = 8 * SCALE
    lot2_right = center_x - 5 * SCALE
    lot1_left = center_x + 5 * SCALE
    lot1_right = width - 5 * SCALE

    out = Path("output/siteplan_dual_lot.svg")
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append(svg_header(width, height))

    # Lot 2 - left side
    lines.append("  <!-- Lot 2 -->")
    lines.append(
        "  "
        + svg_rect(
            Rectangle(0, 0, 467.6, 1102.2),
            fill="none",
            stroke="black",
            **{"stroke-width": 2},
        )
    )
    lines.append(
        "  "
        + svg_text(467.6 / 2, 20, "Lot 2", **{"text-anchor": "middle", "font-size": 14})
    )

    # Lot 1 - right side
    lines.append("  <!-- Lot 1 -->")
    lines.append(
        "  "
        + svg_rect(
            Rectangle(center_x, 0, 450.0, 1101.1),
            fill="none",
            stroke="black",
            **{"stroke-width": 2},
        )
    )
    lines.append(
        "  "
        + svg_text(
            center_x + 225.0,
            20,
            "Lot 1",
            **{"text-anchor": "middle", "font-size": 14},
        )
    )

    lines.append("")
    lines.append("  <!-- Setback lines -->")
    # Lot 2 setbacks
    lines.append(
        "  "
        + svg_line(
            Point(0, front_y),
            Point(center_x, front_y),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  " + svg_text(5, front_y - 5, "18' Front Setback", **{"font-size": 12})
    )
    lines.append(
        "  "
        + svg_line(
            Point(0, rear_y),
            Point(center_x, rear_y),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  " + svg_text(5, rear_y - 6, "11' Rear Setback", **{"font-size": 12})
    )
    lines.append(
        "  "
        + svg_line(
            Point(lot2_left, 0),
            Point(lot2_left, lot2_height),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_left + 5,
            lot2_height / 2,
            "8' Side Setback",
            **{"font-size": 12},
            transform=f"rotate(-90 {lot2_left + 5},{lot2_height / 2})",
        )
    )
    lines.append(
        "  "
        + svg_line(
            Point(lot2_right, 0),
            Point(lot2_right, lot2_height),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_right - 5,
            lot2_height / 2,
            "5' Side Setback",
            **{"font-size": 12},
            transform=f"rotate(-90 {lot2_right - 5},{lot2_height / 2})",
        )
    )

    # Lot 1 setbacks
    lines.append(
        "  "
        + svg_line(
            Point(center_x, front_y),
            Point(width, front_y),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(center_x + 5, front_y - 5, "18' Front Setback", **{"font-size": 12})
    )
    lines.append(
        "  "
        + svg_line(
            Point(center_x, rear_y),
            Point(width, rear_y),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(center_x + 5, rear_y - 6, "11' Rear Setback", **{"font-size": 12})
    )
    lines.append(
        "  "
        + svg_line(
            Point(lot1_left, 0),
            Point(lot1_left, lot1_height),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_left + 5,
            lot1_height / 2,
            "5' Side Setback",
            **{"font-size": 12},
            transform=f"rotate(-90 {lot1_left + 5},{lot1_height / 2})",
        )
    )
    lines.append(
        "  "
        + svg_line(
            Point(lot1_right, 0),
            Point(lot1_right, lot1_height),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_right - 5,
            lot1_height / 2,
            "5' Side Setback",
            **{"font-size": 12},
            transform=f"rotate(-90 {lot1_right - 5},{lot1_height / 2})",
        )
    )

    # Center divider
    lines.append("  <!-- Divider -->")
    lines.append(
        "  " + svg_line(Point(center_x, 0), Point(center_x, height), stroke="black")
    )

    # Street labels
    lines.append(
        "  "
        + svg_text(
            width / 2,
            15,
            "22nd Avenue South (Front)",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_text(
            10,
            height / 2,
            "30th Street South",
            **{"text-anchor": "middle", "font-size": 12},
            transform=f"rotate(-90 10,{height / 2})",
        )
    )
    lines.append(
        "  "
        + svg_text(
            width / 2,
            height - 5,
            "16' Alley (Rear)",
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

    lines.append("")
    lines.append("  <!-- Duplexes -->")
    duplex_w = 33 * SCALE
    duplex_h = 28 * SCALE
    lot2_duplex_x = 67.8
    lot1_duplex_x = 502.6
    duplex_y = front_y
    lines.append(
        "  "
        + svg_rect(
            Rectangle(lot2_duplex_x, duplex_y, duplex_w, duplex_h),
            fill="#ddddff",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_duplex_x + duplex_w / 2,
            duplex_y + duplex_h / 2,
            "Front Duplex (33' × 28', 2-Story)",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_rect(
            Rectangle(lot1_duplex_x, duplex_y, duplex_w, duplex_h),
            fill="#ddddff",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_duplex_x + duplex_w / 2,
            duplex_y + duplex_h / 2,
            "Front Duplex (33' × 28', 2-Story)",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )

    lines.append("")
    lines.append("  <!-- Porches -->")
    porch_w = 6 * SCALE
    porch_h = 10 * SCALE
    porch_y = 120
    lot2_porches = [(67.8, "Porch A (6' × 10')"), (237.8, "Porch B (6' × 10')")]
    lot1_porches = [(502.6, "Porch A (6' × 10')"), (672.6, "Porch B (6' × 10')")]

    for x, label in lot2_porches:
        lines.append(
            "  "
            + svg_rect(
                Rectangle(x, porch_y, porch_w, porch_h),
                fill="#ffeedd",
                stroke="black",
            )
        )
        lines.append(
            "  "
            + svg_text(
                x + porch_w / 2,
                porch_y + porch_h / 2,
                label,
                **{"text-anchor": "middle", "font-size": 10},
            )
        )

    for x, label in lot1_porches:
        lines.append(
            "  "
            + svg_rect(
                Rectangle(x, porch_y, porch_w, porch_h),
                fill="#ffeedd",
                stroke="black",
            )
        )
        lines.append(
            "  "
            + svg_text(
                x + porch_w / 2,
                porch_y + porch_h / 2,
                label,
                **{"text-anchor": "middle", "font-size": 10},
            )
        )

    lines.append(svg_footer())
    out.write_text("\n".join(lines))


if __name__ == "__main__":
    main()

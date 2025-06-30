from __future__ import annotations

from pathlib import Path

from siteplan.geometry import Point, Rectangle
from datetime import date

from siteplan.svg_writer import (
    svg_boundary,
    svg_footer,
    svg_header,
    svg_line,
    svg_polygon,
    svg_rect,
    svg_text,
)

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

    # Title block
    today = date.today().isoformat()
    title_y = 5
    title_h = 90
    lines.append("  <!-- Title Block -->")
    lines.append(
        "  "
        + svg_rect(Rectangle(5, title_y, 380, title_h), fill="#f5f5f5", stroke="black")
    )
    lines.append(
        "  "
        + svg_text(
            10,
            title_y + 20,
            "Site Plan \u2013 Lot 1 &amp; Lot 2 (NTM-1 St Pete)",
            **{"font-size": 14, "font-family": "sans-serif"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            10,
            title_y + 38,
            "2946 &amp; 2948 22nd Ave S, St. Petersburg, FL 33712",
            **{"font-size": 12, "font-family": "sans-serif"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            10,
            title_y + 54,
            "Parcel IDs: 24-31-16-72954-001-0050, 24-31-16-72954-001-0060",
            **{"font-size": 12, "font-family": "sans-serif"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            10,
            title_y + 70,
            "Lots 5 &amp; 6, Block 1, Lakeview Subdivision",
            **{"font-size": 12, "font-family": "sans-serif"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            10,
            title_y + 86,
            f"Prepared: {today}",
            **{"font-size": 12, "font-family": "sans-serif"},
        )
    )

    # North arrow
    lines.append("  <!-- North Arrow -->")
    arrow_top = 40
    lines.append(
        "  "
        + svg_polygon(
            [
                Point(width / 2, arrow_top),
                Point(width / 2 - 10, arrow_top + 20),
                Point(width / 2 + 10, arrow_top + 20),
            ],
            fill="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            width / 2,
            arrow_top + 35,
            "North",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )

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

    # Lot line dimensions
    lines.append(
        "  "
        + svg_text(
            width / 2,
            -5,
            "91.76'",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_text(
            width / 2,
            height + 15,
            "91.76'",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_text(
            -5,
            height / 2,
            "110.22'",
            transform=f"rotate(-90 -5,{height / 2})",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_text(
            width + 5,
            height / 2,
            "110.22'",
            transform=f"rotate(-90 {width + 5},{height / 2})",
            **{"text-anchor": "middle", "font-size": 12},
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

    lines.append("")
    lines.append("  <!-- Buildable Areas -->")
    buildable2 = Rectangle(lot2_left, front_y, lot2_right - lot2_left, rear_y - front_y)
    buildable1 = Rectangle(lot1_left, front_y, lot1_right - lot1_left, rear_y - front_y)
    lines.append(
        "  "
        + svg_boundary(
            buildable2, offset=0, stroke="gray", **{"stroke-dasharray": "4 4"}
        )
    )
    lines.append(
        "  "
        + svg_boundary(
            buildable1, offset=0, stroke="gray", **{"stroke-dasharray": "4 4"}
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

    scale_bar_y = height - 40
    callout_x = width - 265
    callout_y = scale_bar_y - 25
    lines.append("  <!-- Boundary Callout -->")
    lines.append(
        "  "
        + svg_rect(
            Rectangle(callout_x, callout_y, 260, 60),
            fill="white",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_line(
            Point(width - 160, scale_bar_y),
            Point(width - 60, scale_bar_y),
            stroke="black",
            **{"stroke-width": 2},
        )
    )
    lines.append(
        "  "
        + svg_text(
            width - 110,
            scale_bar_y - 5,
            "10'",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )
    lines.append(
        "  "
        + svg_text(
            width - 5,
            scale_bar_y - 15,
            "Scale 1\" = 10'",
            **{"text-anchor": "end", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_text(
            width - 5,
            scale_bar_y + 15,
            "Zoning: NTM-1 (St. Petersburg, FL) \u2013 Setback Compliant \u2713",
            **{"text-anchor": "end", "font-size": 12},
        )
    )

    lines.append("")
    lines.append("  <!-- Duplexes -->")
    duplex_w = 33 * SCALE
    duplex_h = 28 * SCALE
    lot2_duplex_x = 87.8
    lot1_duplex_x = 517.6
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
        + svg_text(
            lot2_duplex_x + duplex_w / 2,
            duplex_y + duplex_h / 2 + 14,
            "Max Height: 24' roofline, 36' peak",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_duplex_x + duplex_w / 2,
            duplex_y + duplex_h + 12,
            "FFE = 9.0'",
            **{"text-anchor": "middle", "font-size": 10},
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
    lines.append(
        "  "
        + svg_text(
            lot1_duplex_x + duplex_w / 2,
            duplex_y + duplex_h / 2 + 14,
            "Max Height: 24' roofline, 36' peak",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_duplex_x + duplex_w / 2,
            duplex_y + duplex_h + 12,
            "FFE = 9.0'",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )

    # Side door for Lot 2 left unit facing 30th Street South
    door_x = lot2_duplex_x
    door_y = 300
    lines.append("  " + svg_rect(Rectangle(door_x, door_y, 5, 10), fill="black"))
    lines.append(
        "  "
        + svg_text(
            door_x - 5,
            door_y + 5,
            "Side Door (Facing 30th St S)",
            **{
                "font-size": 10,
                "text-anchor": "end",
                "transform": f"rotate(-90 {door_x - 5},{door_y + 5})",
            },
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

    lines.append("")
    lines.append("  <!-- Egress Lines -->")
    for x, _ in lot2_porches + lot1_porches:
        lines.append(
            "  "
            + svg_line(
                Point(x + porch_w / 2, porch_y),
                Point(x + porch_w / 2, 0),
                stroke="black",
                **{"stroke-dasharray": "3,3"},
            )
        )

    lines.append("")
    lines.append("  <!-- Garages with ADUs -->")
    adu_w = 30 * SCALE
    adu_h = 20 * SCALE
    adu_y = duplex_y + duplex_h + 20 * SCALE
    lot2_adu_x = 93.8
    lot1_adu_x = 518.8
    lines.append(
        "  "
        + svg_rect(
            Rectangle(lot2_adu_x, adu_y, adu_w, adu_h),
            fill="#ccffcc",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_adu_x + adu_w / 2,
            adu_y + adu_h / 2,
            "Garage with ADU (2BR/1BA)",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_adu_x + adu_w / 2,
            adu_y + adu_h / 2 + 14,
            "Max Height: 20'",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_adu_x + adu_w / 2,
            adu_y + adu_h + 12,
            "FFE = 9.0'",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )
    lines.append(
        "  "
        + svg_rect(
            Rectangle(lot1_adu_x, adu_y, adu_w, adu_h),
            fill="#ccffcc",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_adu_x + adu_w / 2,
            adu_y + adu_h / 2,
            "Garage with ADU (2BR/1BA)",
            **{"text-anchor": "middle", "font-size": 12},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_adu_x + adu_w / 2,
            adu_y + adu_h / 2 + 14,
            "Max Height: 20'",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_adu_x + adu_w / 2,
            adu_y + adu_h + 12,
            "FFE = 9.0'",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )

    lines.append("")
    lines.append("  <!-- A/C Units -->")
    ac_w = 30
    ac_h = 30
    ac_offset = 10
    for adu_x in [lot2_adu_x, lot1_adu_x]:
        ac_x = adu_x + adu_w + ac_offset
        ac_y = adu_y + 20
        lines.append(
            "  "
            + svg_rect(
                Rectangle(ac_x, ac_y, ac_w, ac_h),
                fill="#cccccc",
                stroke="black",
            )
        )
        lines.append(
            "  "
            + svg_text(
                ac_x + ac_w / 2,
                ac_y + ac_h / 2,
                "A/C Unit",
                **{"text-anchor": "middle", "font-size": 10},
            )
        )

    lines.append("")
    lines.append("  <!-- Drainage Arrows -->")
    for mid_x in [center_x / 2, center_x + (width - center_x) / 2]:
        start_y = rear_y - 150
        end_y = rear_y - 20
        lines.append(
            "  " + svg_line(Point(mid_x, start_y), Point(mid_x, end_y), stroke="blue")
        )
        lines.append(
            "  "
            + svg_polygon(
                [
                    Point(mid_x - 5, end_y - 10),
                    Point(mid_x + 5, end_y - 10),
                    Point(mid_x, end_y),
                ],
                fill="blue",
            )
        )

    lines.append("")
    lines.append("  <!-- ADU Stairs -->")
    for adu_x in [lot2_adu_x, lot1_adu_x]:
        base_x = adu_x + adu_w / 2
        base_y = adu_y + adu_h
        lines.append(
            "  "
            + svg_line(
                Point(base_x, base_y),
                Point(base_x, base_y + 20),
                stroke="black",
            )
        )
        lines.append(
            "  "
            + svg_polygon(
                [
                    Point(base_x - 5, base_y + 20),
                    Point(base_x + 5, base_y + 20),
                    Point(base_x, base_y + 30),
                ],
                fill="black",
            )
        )
        lines.append(
            "  "
            + svg_text(
                base_x,
                base_y + 35,
                "Stairs",
                **{"text-anchor": "middle", "font-size": 10},
            )
        )

    lines.append("")
    lines.append("  <!-- Parking Pads -->")
    pad_w = 9 * SCALE
    pad_h = 20 * SCALE
    pad_y = adu_y + adu_h
    lot2_pads = [93.8, 193.8, 293.8]
    lot1_pads = [518.8, 618.8, 718.8]

    for idx, x in enumerate(lot2_pads, 1):
        lines.append(
            "  "
            + svg_rect(
                Rectangle(x, pad_y, pad_w, pad_h),
                fill="#ffff99",
                stroke="black",
            )
        )
        lines.append(
            "  "
            + svg_text(
                x + pad_w / 2,
                pad_y + pad_h / 2,
                f"P{idx}",
                **{"text-anchor": "middle", "font-size": 10},
            )
        )

    for idx, x in enumerate(lot1_pads, 1):
        lines.append(
            "  "
            + svg_rect(
                Rectangle(x, pad_y, pad_w, pad_h),
                fill="#ffff99",
                stroke="black",
            )
        )
        lines.append(
            "  "
            + svg_text(
                x + pad_w / 2,
                pad_y + pad_h / 2,
                f"P{idx}",
                **{"text-anchor": "middle", "font-size": 10},
            )
        )

    lines.append("")
    lines.append("  <!-- Trash Pads -->")
    trash_w = 6 * SCALE
    trash_h = 20 * SCALE
    trash_y = pad_y
    lot2_trash_x = 390
    lot1_trash_x = 880
    lines.append(
        "  "
        + svg_rect(
            Rectangle(lot2_trash_x, trash_y, trash_w, trash_h),
            fill="#deb887",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot2_trash_x + trash_w / 2,
            trash_y + trash_h / 2,
            "Trash Pad (6' × 20')",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )
    lines.append(
        "  "
        + svg_rect(
            Rectangle(lot1_trash_x, trash_y, trash_w, trash_h),
            fill="#deb887",
            stroke="black",
        )
    )
    lines.append(
        "  "
        + svg_text(
            lot1_trash_x + trash_w / 2,
            trash_y + trash_h / 2,
            "Trash Pad (6' × 20')",
            **{"text-anchor": "middle", "font-size": 10},
        )
    )

    lines.append(svg_footer())
    out.write_text("\n".join(lines))


if __name__ == "__main__":
    main()

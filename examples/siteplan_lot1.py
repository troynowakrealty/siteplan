from __future__ import annotations

from pathlib import Path

from siteplan.geometry import Point, Rectangle
from siteplan.svg_writer import svg_footer, svg_header, svg_line, svg_rect, svg_text

SCALE = 10


def main() -> None:
    width = 45 * SCALE
    height = 110.11 * SCALE
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
            Point(0, 180),
            Point(width, 180),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append("  " + svg_text(5, 175, "Front setback 18'", **{"font-size": 12}))

    rear_y = height - 110
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
            Point(80, 0),
            Point(80, height),
            stroke="blue",
            **{"stroke-dasharray": "5,5"},
        )
    )
    lines.append(
        "  "
        + svg_text(
            85,
            height / 2,
            "Left setback 8'",
            **{"font-size": 12},
            transform=f"rotate(-90 85,{height / 2})",
        )
    )

    right_x = width - 50
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
        "  " + svg_rect(Rectangle(80, 180, 330, 280), fill="#dddddd", stroke="black")
    )
    lines.append(
        "  "
        + svg_text(245, 320, "Duplex", **{"text-anchor": "middle", "font-size": 14})
    )

    lines.append("")
    lines.append("  <!-- ADU -->")
    adu_y = rear_y - 200
    lines.append(
        "  " + svg_rect(Rectangle(80, adu_y, 300, 200), fill="#cccccc", stroke="black")
    )
    lines.append(
        "  "
        + svg_text(
            230,
            adu_y + 100,
            "ADU",
            **{"text-anchor": "middle", "font-size": 14},
        )
    )

    lines.append("")
    lines.append("  <!-- Parking Pads -->")
    lines.append(
        "  " + svg_rect(Rectangle(80, 460, 90, 200), fill="#eeeeee", stroke="black")
    )
    lines.append(
        "  "
        + svg_text(125, 560, "Parking 1", **{"text-anchor": "middle", "font-size": 12})
    )
    lines.append(
        "  " + svg_rect(Rectangle(170, 460, 90, 200), fill="#eeeeee", stroke="black")
    )
    lines.append(
        "  "
        + svg_text(215, 560, "Parking 2", **{"text-anchor": "middle", "font-size": 12})
    )
    lines.append(
        "  " + svg_rect(Rectangle(260, 460, 90, 200), fill="#eeeeee", stroke="black")
    )
    lines.append(
        "  "
        + svg_text(305, 560, "Parking 3", **{"text-anchor": "middle", "font-size": 12})
    )

    lines.append("")
    lines.append("  <!-- Trash Pad -->")
    lines.append(
        "  " + svg_rect(Rectangle(350, 460, 60, 200), fill="#eeeeee", stroke="black")
    )
    lines.append(
        "  " + svg_text(380, 560, "Trash", **{"text-anchor": "middle", "font-size": 12})
    )

    lines.append(svg_footer())
    out.write_text("\n".join(lines))


if __name__ == "__main__":
    main()

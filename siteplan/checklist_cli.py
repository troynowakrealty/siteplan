from __future__ import annotations

from pathlib import Path

from .geometry import Rectangle
from .layout import Layout
from .optimizer import apply_constraints, separate_shapes


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Interactive siteplan generator")
    parser.add_argument(
        "output",
        nargs="?",
        default="output/siteplan.svg",
        help="Output SVG file",
    )
    parser.add_argument(
        "--font-size",
        type=int,
        default=12,
        help="Font size for dimension labels",
    )
    args = parser.parse_args()

    layout = Layout()
    placements = []

    prop_w_str = input("Property width in ft (blank for none): ").strip()
    prop_h_str = input("Property height in ft (blank for none): ").strip()
    prop_w = float(prop_w_str) * 10 if prop_w_str else None
    prop_h = float(prop_h_str) * 10 if prop_h_str else None

    num_shapes = int(input("How many shapes? "))
    for i in range(num_shapes):
        print(f"Shape {i + 1}")
        width = float(input("  width (ft): ")) * 10
        height = float(input("  height (ft): ")) * 10
        x = float(input("  x position (ft): ")) * 10
        y = float(input("  y position (ft): ")) * 10
        orientation = input(
            "  orientation [north|south|east|west] (default north): "
        ).strip()
        orientation = orientation or "north"
        left = float(input("  left setback (ft, default 0): ") or 0) * 10
        right = float(input("  right setback (ft, default 0): ") or 0) * 10
        top = float(input("  top setback (ft, default 0): ") or 0) * 10
        bottom = float(input("  bottom setback (ft, default 0): ") or 0) * 10

        layout.add_shape(Rectangle(x, y, width, height))
        placement = {
            "setbacks": {
                "left": left,
                "right": right,
                "top": top,
                "bottom": bottom,
            },
            "facing": orientation,
        }
        if prop_w is not None:
            placement["property_width"] = prop_w
        if prop_h is not None:
            placement["property_height"] = prop_h
        placements.append(placement)

    apply_constraints(layout, placements)
    separate_shapes(layout)

    layout.export_svg(Path(args.output), font_size=args.font_size)


if __name__ == "__main__":
    main()

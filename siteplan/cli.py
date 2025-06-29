from __future__ import annotations

from pathlib import Path

from .geometry import Rectangle
from .layout import Layout


def main(output: str = "output/siteplan.svg") -> None:
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 100, 50))
    layout.add_shape(Rectangle(120, 0, 80, 40))
    layout.export_svg(Path(output))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a simple site plan SVG")
    parser.add_argument(
        "output",
        nargs="?",
        default="output/siteplan.svg",
        help="Output SVG path",
    )
    args = parser.parse_args()
    main(args.output)

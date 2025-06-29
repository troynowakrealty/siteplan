import argparse
from pathlib import Path

from . import layout, svg_writer


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Generate duplex + ADU site plan")
    parser.add_argument(
        "--output",
        default="output/duplex_siteplan.svg",
        help="Path to output SVG file",
    )
    args = parser.parse_args(argv)

    shapes = layout.generate_siteplan()
    output = Path(args.output)
    svg_writer.write_svg(shapes, output)
    print(f"SVG written to {output}")


if __name__ == "__main__":
    main()

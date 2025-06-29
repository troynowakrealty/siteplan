import argparse

from layout import generate_svg


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate site plan SVG")
    parser.add_argument(
        "--output", default="output/siteplan.svg", help="Path to output SVG"
    )
    args = parser.parse_args()
    generate_svg(args.output)


if __name__ == "__main__":
    main()

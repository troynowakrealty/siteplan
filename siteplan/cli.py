from __future__ import annotations

from pathlib import Path

from .geometry import Rectangle
from .layout import Layout
from .optimizer import separate_shapes
from .prompt_parser import parse_prompt


def main(output: str = "output/siteplan.svg", prompt: str | None = None) -> None:
    layout = Layout()
    if prompt:
        rects = parse_prompt(prompt)
        for r in rects:
            layout.add_shape(r)
    else:
        layout.add_shape(Rectangle(0, 0, 100, 50))
        layout.add_shape(Rectangle(120, 0, 80, 40))

    separate_shapes(layout)
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
    parser.add_argument(
        "--prompt",
        help="Prompt text or @path to file containing prompt",
    )
    args = parser.parse_args()

    prompt_text = None
    if args.prompt:
        if args.prompt.startswith("@"):
            prompt_text = Path(args.prompt[1:]).read_text()
        else:
            prompt_text = args.prompt

    main(args.output, prompt_text)

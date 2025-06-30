from __future__ import annotations

from pathlib import Path

from .geometry import Rectangle
from .layout import Layout
from .optimizer import separate_shapes
from .prompt_parser import parse_prompt


def main(
    output: str = "output/siteplan.svg",
    prompt: str | None = None,
    load: str | None = None,
    append_prompt: str | None = None,
) -> None:
    if load:
        layout = Layout.load(Path(load))
    else:
        layout = Layout()
        if prompt:
            rects = parse_prompt(prompt)
            for r in rects:
                layout.add_shape(r)
        else:
            layout.add_shape(Rectangle(0, 0, 100, 50))
            layout.add_shape(Rectangle(120, 0, 80, 40))

    if append_prompt:
        for r in parse_prompt(append_prompt):
            layout.add_shape(r)

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
    parser.add_argument(
        "--load",
        help="Path to Layout JSON or pickle to load",
    )
    parser.add_argument(
        "--append-prompt",
        help="Additional prompt instructions to apply",
    )
    args = parser.parse_args()

    prompt_text = None
    if args.prompt:
        if args.prompt.startswith("@"):
            prompt_text = Path(args.prompt[1:]).read_text()
        else:
            prompt_text = args.prompt

    append_text = None
    if args.append_prompt:
        if args.append_prompt.startswith("@"):
            append_text = Path(args.append_prompt[1:]).read_text()
        else:
            append_text = args.append_prompt

    main(
        args.output,
        prompt_text,
        load=args.load,
        append_prompt=append_text,
    )

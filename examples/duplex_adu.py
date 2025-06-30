from pathlib import Path

from siteplan.layout import Layout
from siteplan.optimizer import separate_shapes
from siteplan.prompt_parser import parse_prompt

PROMPT = """
place duplex 40x30 at 0,0
place adu 20x20 at 50,0
"""


def main() -> None:
    layout = Layout()
    for placement in parse_prompt(PROMPT):
        layout.add_shape(placement.rect)
    separate_shapes(layout)
    layout.export_svg(Path("output/examples/duplex_adu.svg"))


if __name__ == "__main__":
    main()

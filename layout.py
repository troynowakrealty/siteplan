import os
from typing import Dict, Tuple

from geometry import ft_to_px, rect_pixels

DUPLEX_SIZE = (30, 40)  # width_ft, height_ft
ADU_SIZE = (20, 20)
SPACING = 10  # feet between buildings


def layout_positions() -> Dict[str, Tuple[float, float, float, float]]:
    """Return pixel rectangles for duplex and ADU."""
    duplex_origin = (0, 0)
    adu_origin = (DUPLEX_SIZE[0] + SPACING, 0)
    return {
        "duplex": rect_pixels(duplex_origin, *DUPLEX_SIZE),
        "adu": rect_pixels(adu_origin, *ADU_SIZE),
    }


def generate_svg(path: str = "output/siteplan.svg") -> None:
    """Generate simple SVG drawing to *path*."""
    positions = layout_positions()
    width_ft = DUPLEX_SIZE[0] + SPACING + ADU_SIZE[0]
    height_ft = max(DUPLEX_SIZE[1], ADU_SIZE[1])
    width_px = ft_to_px(width_ft)
    height_px = ft_to_px(height_ft)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width_px}" height="{height_px}">'
    ]
    for name, (x, y, w, h) in positions.items():
        color = "blue" if name == "duplex" else "green"
        lines.append(
            f'<rect id="{name}" x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" />'
        )
    lines.append("</svg>")

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

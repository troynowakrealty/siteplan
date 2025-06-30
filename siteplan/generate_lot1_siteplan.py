from siteplan.geometry import Rectangle
from siteplan.svg_writer import svg_rect, svg_header, svg_footer
import os

output_path = "output/siteplan_lot1.svg"
os.makedirs("output", exist_ok=True)

LOT_WIDTH = 46.76
LOT_DEPTH = 110.22

def text(x, y, label, size=1.5, rotate=None):
    rotate_attr = f" transform='rotate({rotate},{x},{y})'" if rotate else ""
    return f"<text x='{x}' y='{y}' font-size='{size}' fill='black'{rotate_attr}>{label}</text>"

def line(x1, y1, x2, y2, stroke='black', dash=None, width=0.25):
    dash_attr = f" stroke-dasharray='{dash}'" if dash else ""
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{stroke}' stroke-width='{width}'{dash_attr}/>\n"

with open(output_path, "w") as f:
    f.write(svg_header(width="9in", height="11in", viewBox=f"0 0 {LOT_WIDTH} {LOT_DEPTH}") + "\n")

    # Lot boundary (bold)
    lot = Rectangle(0, 0, LOT_WIDTH, LOT_DEPTH)
    f.write(svg_rect(lot, stroke="black", fill="none", stroke_width="2") + "\n")

    # Setbacks
    f.write(line(0, 18, LOT_WIDTH, 18, stroke="red", dash="4,2"))  # front
    f.write(text(1, 17, "18′ Front Setback"))

    f.write(line(0, LOT_DEPTH - 11, LOT_WIDTH, LOT_DEPTH - 11, stroke="red", dash="4,2"))  # rear
    f.write(text(1, LOT_DEPTH - 12, "11′ Rear Setback"))

    f.write(line(8, 0, 8, LOT_DEPTH, stroke="red", dash="4,2"))  # left
    f.write(text(8.5, 5, "8′ Side Setback", rotate=-90))

    f.write(line(LOT_WIDTH - 5, 0, LOT_WIDTH - 5, LOT_DEPTH, stroke="red", dash="4,2"))  # right
    f.write(text(LOT_WIDTH - 4.5, 5, "5′ Setback", rotate=-90))

    # Duplex
    duplex = Rectangle(8, 18, 33, 28)
    f.write(svg_rect(duplex, stroke="blue", fill="#ddddff", stroke_width="0.5") + "\n")
    f.write(text(duplex.x + 2, duplex.y + 14, "Front Duplex (2-story)"))
    f.write(text(duplex.x + 2, duplex.y + 8, "Unit A"))
    f.write(text(duplex.x + 18, duplex.y + 8, "Unit B"))
    f.write(text(duplex.x + 10, duplex.y + 26, "33′ × 28′"))

    # Porches
    porch_a = Rectangle(8, 12, 10, 6)
    porch_b = Rectangle(31, 12, 10, 6)
    f.write(svg_rect(porch_a, stroke="gray", fill="#cccccc", stroke_dasharray="2,2") + "\n")
    f.write(svg_rect(porch_b, stroke="gray", fill="#cccccc", stroke_dasharray="2,2") + "\n")
    f.write(text(porch_a.x + 1, porch_a.y + 4, "Porch A"))
    f.write(text(porch_b.x + 1, porch_b.y + 4, "Porch B"))

    # Garage with ADU
    garage = Rectangle(8, 74, 30, 20)
    f.write(svg_rect(garage, stroke="green", fill="#ddffdd", stroke_width="0.5") + "\n")
    f.write(text(garage.x + 1, garage.y + 8, "Garage with ADU (2BR/1BA)"))
    f.write(text(garage.x + 8, garage.y + 18, "30′ × 20′"))

    # Separation line
    f.write(line(24.5, 46, 24.5, 74, stroke="black", dash="2,2"))
    f.write(text(25, 62, "28′ between structures"))

    # Parking spots
    for i in range(3):
        px = 8 + i * 9
        stall = Rectangle(px, LOT_DEPTH - 20, 9, 20)
        f.write(svg_rect(stall, stroke="gold", fill="none", stroke_width="0.5") + "\n")
        f.write(text(px + 1.5, LOT_DEPTH - 10, f"P{i + 1}"))

    # Trash pad
    trash = Rectangle(35, LOT_DEPTH - 20, 6, 20)
    f.write(svg_rect(trash, stroke="brown", fill="none", stroke_dasharray="3,2") + "\n")
    f.write(text(trash.x + 0.5, trash.y + 10, "Trash Pad 6×20"))

    # Dimension lines
    f.write(line(0, -1, LOT_WIDTH, -1))
    f.write(text(LOT_WIDTH / 2 - 3, -2, f"{LOT_WIDTH}′ width"))

    f.write(line(LOT_WIDTH + 1, 0, LOT_WIDTH + 1, LOT_DEPTH))
    f.write(text(LOT_WIDTH + 2, LOT_DEPTH / 2, f"{LOT_DEPTH}′ depth", rotate=-90))

    # Scale bar
    f.write(line(2, LOT_DEPTH + 2, 12, LOT_DEPTH + 2, width=0.5))
    f.write(line(2, LOT_DEPTH + 1.8, 2, LOT_DEPTH + 2.2))
    f.write(line(7, LOT_DEPTH + 1.8, 7, LOT_DEPTH + 2.2))
    f.write(line(12, LOT_DEPTH + 1.8, 12, LOT_DEPTH + 2.2))
    f.write(text(1.5, LOT_DEPTH + 3.5, "Scale: 1\" = 10′"))
    f.write(text(2, LOT_DEPTH + 3, "0′"))
    f.write(text(7, LOT_DEPTH + 3, "5′"))
    f.write(text(12, LOT_DEPTH + 3, "10′"))

    # North arrow
    f.write(f"<text x='{LOT_WIDTH / 2 - 1}' y='-4' font-size='3'>↑ N</text>\n")

    # Title block
    f.write(svg_rect(Rectangle(LOT_WIDTH - 18, LOT_DEPTH + 5, 17, 5), stroke="black", fill="none") + "\n")
    f.write(text(LOT_WIDTH - 17.5, LOT_DEPTH + 6, "Site Plan – Lot 1"))
    f.write(text(LOT_WIDTH - 17.5, LOT_DEPTH + 7.5, "2946 22nd Ave S"))
    f.write(text(LOT_WIDTH - 17.5, LOT_DEPTH + 9, "Date: June 2025"))
    f.write(text(LOT_WIDTH - 17.5, LOT_DEPTH + 10.5, "Scale: 1\" = 10′"))

    f.write(svg_footer())

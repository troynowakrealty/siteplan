from siteplan.geometry import Rectangle, Point
from siteplan.svg_writer import svg_rect, svg_line, svg_header, svg_footer, svg_tag
import os

W, D = 46.76, 110.22
output = "output/siteplan_lot1_blueprint.svg"
os.makedirs("output", exist_ok=True)

def text(x, y, t, size=1.5, rot=None):
    r = f" transform='rotate({rot},{x},{y})'" if rot else ""
    return f"<text x='{x}' y='{y}' font-size='{size}'{r}>{t}</text>\n"

def door(x, y, orient="horizontal"):
    if orient == "horizontal":
        return f"<line x1='{x}' y1='{y}' x2='{x + 1}' y2='{y}' stroke='black' stroke-width='0.5' />\n"
    else:
        return f"<line x1='{x}' y1='{y}' x2='{x}' y2='{y + 1}' stroke='black' stroke-width='0.5' />\n"

with open(output,"w") as f:
    f.write(svg_header(width="9in", height="11in", viewBox=f"0 0 {W} {D}") + "\n")

    # Lot outline
    f.write(svg_rect(Rectangle(0,0,W,D),stroke="black",fill="none",stroke_width="2")+"\n")

    # Front Duplex – centered
    duplex_x = 8 + (W - 8 - 5 - 33)/2
    duplex = Rectangle(duplex_x, 18, 33, 28)
    f.write(svg_rect(duplex, stroke="black", fill="#f2f2f2", stroke_width="1.5") + "\n")
    f.write(text(duplex.x + 10, duplex.y + 15, "Front Duplex (2-story)"))
    f.write(text(duplex.x + 2, duplex.y + 8, "Unit A"))
    f.write(text(duplex.x + 20, duplex.y + 8, "Unit B"))
    f.write(text(duplex.x + 10, duplex.y + 26, "33′ × 28′"))

    # Porches
    porch_a = Rectangle(duplex.x + 2, 12, 8.5, 6)
    porch_b = Rectangle(duplex.x + 22.5, 12, 8.5, 6)
    for porch in [porch_a, porch_b]:
        f.write(svg_rect(porch, stroke="blue", fill="none", stroke_dasharray="2,2") + "\n")
    f.write(text(porch_a.x + 0.5, porch_a.y + 3, "Porch A"))
    f.write(text(porch_b.x + 0.5, porch_b.y + 3, "Porch B"))

    # Duplex Doors
    f.write(door(porch_a.x + 4, porch_a.y + 5))  # Unit A facing 30th
    f.write(door(porch_b.x + 4, porch_b.y + 5))  # Unit B facing 22nd

    # Garage with ADU
    garage = Rectangle(8, 68, 30, 20)
    f.write(svg_rect(garage, stroke="black", fill="#e0ffe0", stroke_width="1.5") + "\n")
    f.write(text(garage.x + 2, garage.y + 10, "Garage + ADU"))
    f.write(text(garage.x + 6, garage.y + 18, "30′ × 20′"))

    # ADU Door (rear)
    f.write(door(garage.x + 28, garage.y + 10, orient="vertical"))

    # Parking Spots (3ft setback from rear)
    for i in range(3):
        px = 8 + i * 9
        py = 92.22
        f.write(svg_rect(Rectangle(px, py, 9, 18), stroke="gold", fill="none", stroke_width="0.5") + "\n")
        f.write(text(px + 2, py + 9, f"P{i+1}"))
    f.write(text(8, 111, "Parking - 3′ ROW offset"))

    # Trash Pad
    f.write(svg_rect(Rectangle(35, 92.22, 6, 18), stroke="brown", fill="none", stroke_dasharray="3,2") + "\n")
    f.write(text(35.5, 100, "Trash Pad"))

    # North Arrow
    f.write(svg_tag("polygon", points="45,5 46,2 47,5", fill="black") + "\n")
    f.write(text(45.5, 7, "N"))

    # Title
    f.write(text(1, -2, "Site Plan – Lot 1, 2946 22nd Ave S"))
    f.write(text(1, -0.5, "Date: June 2025 | Scale: 1\" = 10′"))

    f.write(svg_footer())

from siteplan.geometry import Rectangle
from siteplan.svg_writer import svg_header, svg_footer, svg_rect, svg_line, svg_tag
import os

W, D = 46.76, 110.22
output = "output/siteplan_lot1_blueprint_pro.svg"
os.makedirs("output", exist_ok=True)

def text(x, y, t, size=1.2, rot=None):
    rot_attr = f" transform='rotate({rot},{x},{y})'" if rot else ""
    return f"<text x='{x}' y='{y}' font-size='{size}'{rot_attr}>{t}</text>\n"

def swing_arc(cx, cy, r, start_deg, end_deg):
    # SVG arc path format: M start, A radius, large-arc-flag sweep-flag to end
    from math import radians, cos, sin
    x1, y1 = cx + r * cos(radians(start_deg)), cy + r * sin(radians(start_deg))
    x2, y2 = cx + r * cos(radians(end_deg)), cy + r * sin(radians(end_deg))
    return f"<path d='M{x1:.2f},{y1:.2f} A{r},{r} 0 0,1 {x2:.2f},{y2:.2f}' stroke='black' fill='none' stroke-width='0.5'/>\n"

with open(output, "w") as f:
    f.write(svg_header(width="9in", height="11in", viewBox=f"0 0 {W} {D}") + "\n")
    # Draw setbacks first
    for y, label in [(18, "18′ Front"), (D-11, "11′ Rear")]:
        f.write(svg_line(Rectangle(0, y, 0, 0), Rectangle(W, y, 0, 0), stroke="red", stroke_dasharray="4,2") + text(1, y-0.5, label))
    for x, label in [(8, "8′ Side"), (W-5, "5′ Interior")]:
        f.write(svg_line(Rectangle(x, 0, 0, 0), Rectangle(x, D, 0, 0), stroke="red", stroke_dasharray="4,2") + text(x+0.3, 1, label, rot=-90))
    # Lot boundary
    f.write(svg_rect(Rectangle(0, 0, W, D), stroke="black", fill="none", stroke_width="2") + "\n")
    # Duplex centered between setbacks
    duplex_x = 8 + (W - 8 - 5 - 33)/2
    duplex = Rectangle(duplex_x, 18, 33, 28)
    f.write(svg_rect(duplex, stroke="black", fill="#f2f2f2", stroke_width="1.5"))
    f.write(text(duplex.x+5, duplex.y+22, "Front Duplex (2‑story)"))
    f.write(text(duplex.x+2, duplex.y+8, "Unit A"))
    f.write(text(duplex.x+20, duplex.y+8, "Unit B"))
    # Swing-arc doors
    f.write(swing_arc(duplex.x+4, duplex.y+12, 3, -90, 0))  # Unit A faces side
    f.write(swing_arc(duplex.x+29, duplex.y+12, 3, 180, 90))  # Unit B faces front
    # Porches
    for px in (duplex.x+2, duplex.x+22.5):
        f.write(svg_rect(Rectangle(px, 12, 8.5, 6), stroke="black", fill="none", stroke_dasharray="2,2"))
    # Garage + ADU
    garage = Rectangle(8, 68, 30, 20)
    f.write(svg_rect(garage, stroke="black", fill="#dcedc8", stroke_width="1.5"))
    f.write(text(garage.x+5, garage.y+10, "Garage + ADU"))
    # Garage door (swing)
    f.write(swing_arc(garage.x+28, garage.y+10, 3, 90, 0))
    # Parking stalls behind garage
    for i in range(3):
        px = 8 + i * 9
        stall = Rectangle(px, 91.22, 9, 18)  # 3 ft ROW setback
        f.write(svg_rect(stall, stroke="gold", fill="none", stroke_width="1"))
        f.write(text(px+2, stall.y+10, f"P{i+1}"))
    f.write(text(1, 109, "Parking setbacks + driveway width meets 10–20′"))    
    # Trash pad
    f.write(svg_rect(Rectangle(35, 91.22, 6, 18), stroke="brown", fill="none", stroke_dasharray="3,2"))
    f.write(text(35.5, 100, "Trash Pad 6′×20′"))
    # North arrow (compass)
    f.write(svg_tag("circle", self_close=True, cx="45", cy="10", r="3", stroke="black", fill="none", stroke_width="0.5"))
    f.write(svg_tag("polygon", self_close=True, points="45,6 44,10 46,10", fill="black"))
    f.write(text(45, 15, "N", size=1.5))
    # Scale bar
    f.write(svg_line(Rectangle(2, D+2, 0, 0), Rectangle(12, D+2, 0, 0), stroke="black", stroke_width="0.5"))
    for x in [2,7,12]:
        f.write(svg_line(Rectangle(x, D+1.8, 0, 0), Rectangle(x, D+2.2, 0, 0), stroke="black", stroke_width="0.5"))
    f.write(text(1.5, D+4, "0′"))
    f.write(text(7, D+4, "5′"))
    f.write(text(12, D+4, "10′"))
    f.write(text(2, D+5, 'Scale: 1" = 10′'))
    # Titles & notes
    f.write(text(1, -2, "Site Plan – Lot 1, 2946 22nd Ave S"))
    f.write(text(1, -0.5, 'Date: June 2025 | Blueprint‑style'))
    # Title block & legend
    tb_x = W-18; tb_y = D+5
    f.write(svg_rect(Rectangle(tb_x, tb_y, 17, 5), stroke="black", fill="none", stroke_width="0.5"))
    f.write(text(tb_x+0.2, tb_y+1.5, "Scale: 1\" = 10′"))
    f.write(text(tb_x+0.2, tb_y+3, "FAR 1,524/2,886 ft²"))
    legend_y = tb_y
    for i, (lbl,clr) in enumerate([("Building","#f2f2f2"),("ADU","#dcedc8"),("Porch","none"),("Park","none"),("Trash","none")]):
        y = legend_y + 6 + i*1
        f.write(svg_rect(Rectangle(2, y, 1, 1), stroke="black", fill=clr, stroke_width="0.5"))
        f.write(text(4, y+0.8, lbl))
    f.write(svg_footer())

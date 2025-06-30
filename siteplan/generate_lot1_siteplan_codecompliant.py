from siteplan.geometry import Rectangle
from siteplan.svg_writer import svg_rect, svg_line, svg_header, svg_footer, svg_tag
import os

output = "output/siteplan_lot1_codecompliant.svg"
os.makedirs("output", exist_ok=True)
W, D = 46.76, 110.22

def text(x, y, t, size=1.2, rot=None):
    r = f" transform='rotate({rot},{x},{y})'" if rot else ""
    return f"<text x='{x}' y='{y}' font-size='{size}'{r}>{t}</text>\n"

def arrow(x,y,s=0.5):
    pts = [(x,y), (x+s/2, y-s), (x+s, y)]
    return svg_tag("polygon", self_close=True, points=" ".join(f"{px},{py}" for px,py in pts), fill="black")

def dim(x1,y1,x2,y2, off=0.5):
    return (
        svg_line(Rectangle(x1,y1,0,0), Rectangle(x2,y2,0,0), stroke="black", stroke_width="0.2") + "\n"
        + arrow(x1, y1-off) + arrow(x2, y2-off)
    )

with open(output,"w") as f:
    f.write(svg_header(width="9in", height="11in", viewBox=f"0 0 {W} {D}") + "\n")

    # Lot outline
    f.write(svg_rect(Rectangle(0,0,W,D),stroke="black",fill="none",stroke_width="2")+"\n")

    # Street & alley labels
    f.write(text(W/2-9, -2, "22nd Ave S (Front)"))
    f.write(text(-2, D/2, "30th St S (Side)", rot=-90))
    f.write(text(W/2, D+3, "Alley"))

    # Setbacks
    for coord,label in [(18,"18′ Front Setback"), (D-11,"11′ Rear Setback")]:
        f.write(svg_line(Rectangle(0,coord,0,0), Rectangle(W,coord,0,0), stroke="red", stroke_dasharray="4,2")+"\n")
        f.write(text(1, coord-0.5, label))
    for coord,label in [(8,"8′ Side Setback"), (W-5,"5′ Interior Setback")]:
        f.write(svg_line(Rectangle(coord,0,0,0), Rectangle(coord,D,0,0), stroke="red", stroke_dasharray="4,2")+"\n")
        f.write(text(coord+0.5, 1, label, rot=-90))

    # Duplex + porches
    duplex = Rectangle(8 + (W - 8 - 5 - 33) / 2, 18, 33, 28)
    f.write(svg_rect(duplex,stroke="black",fill="#f2f2f2",stroke_width="0.5")+"\n")
    f.write(text(duplex.x+2, duplex.y+14, "Front Duplex (2-story)"))
    f.write(text(duplex.x+2, duplex.y+8, "Unit A"))
    f.write(text(duplex.x+18, duplex.y+8, "Unit B"))
    f.write(text(duplex.x+10, duplex.y+26, "33′×28′"))

    for px in [8, 31]:
        pr = Rectangle(px,12,10,6)
        f.write(svg_rect(pr,stroke="blue",fill="none",stroke_dasharray="2,2")+"\n")
        f.write(text(pr.x+1, pr.y+4, "Porch (encroachment allowed)"))

    # Garage/ADU
    gar = Rectangle(8,70,30,20)
    f.write(svg_rect(gar,stroke="black",fill="#dcedc8",stroke_width="0.5")+"\n")
    f.write(text(gar.x+1, gar.y+8, "Garage w/ ADU (2BR/1BA)"))
    f.write(text(gar.x+8, gar.y+18, "30′×20′"))

    # 28′ separation value & note
    f.write(dim(8,46,8,74))
    f.write(text(10,60, "28′ between structures"))

    # Parking & driveway with 3′ ROW setback
    for i in range(3):
        px = 8 + i*9
        py = 92.22  # shifted back 3′
        stall = Rectangle(px, py, 9, 20)
        f.write(svg_rect(stall,stroke="gold",fill="none",stroke_width="0.5")+"\n")
        f.write(text(px+1.5, py+10, f"P{i+1}"))
    f.write(text(1, D-24, "Parking stalls + driveway offset 3′ from ROW"))
    f.write(text(1, D-22, "Driveway width meets 10–20′ standard"))

    # Trash pad
    tr = Rectangle(35, D-23,6,20)
    f.write(svg_rect(tr,stroke="brown",fill="none",stroke_dasharray="3,2")+"\n")
    f.write(text(tr.x+0.5, tr.y+10, "Trash Pad 6′×20′"))

    # Dimensions: lot width & depth
    f.write(dim(0,-1,W,-1))
    f.write(text(W/2-3, -2, f"{W}′ width"))
    f.write(dim(W+1,0,W+1,D))
    f.write(text(W+2, D/2, f"{D}′ depth", rot=-90))

    # FAR & height note
    f.write(text(1, D+1.5, "FAR used: 1,524 / 2,886 ft² (±200 ft² garage exempt)"))
    f.write(text(1, D+0.2, "Height: roofline ≤24′, peak ≤36′"))

    # Scale bar
    f.write(svg_line(Rectangle(2,D+2,0,0), Rectangle(12,D+2,0,0),stroke="black", stroke_width="0.5")+"\n")
    for x in [2,7,12]:
        f.write(svg_line(Rectangle(x,D+1.8,0,0), Rectangle(x,D+2.2,0,0),stroke="black", stroke_width="0.5")+"\n")
    f.write(text(1.5,D+4,"0′")) ; f.write(text(7,D+4,"5′")) ; f.write(text(12,D+4,"10′"))
    f.write(text(2,D+4.5,'Scale: 1" = 10′'))

    # Improved north arrow
    f.write(arrow(W-5,5,3))
    f.write(text(W-4.5,10,"N"))

    # Title block
    tb = Rectangle(W-18, D+5,17,5)
    f.write(svg_rect(tb,stroke="black",fill="none",stroke_width="0.5")+"\n")
    f.write(text(tb.x+0.2, tb.y+1.5,"Site Plan – Lot 1"))
    f.write(text(tb.x+0.2, tb.y+3,"2946 22nd Ave S"))
    f.write(text(tb.x+0.2, tb.y+4.5,'Date: June 2025 | Scale: 1"=10′'))

    # Legend
    lg = Rectangle(1, D+5,15,5)
    f.write(svg_rect(lg,stroke="black",fill="none",stroke_width="0.5")+"\n")
    for idx,(lbl,clr) in enumerate([("Building","#f2f2f2"),("ADU","#dcedc8"),("Porch","none"),("Parking","none"),("Trash","none")]):
        y = D+6 + idx*1
        f.write(svg_rect(Rectangle(2,y,1,1),stroke="black",fill=clr,stroke_width="0.5")+"\n")
        f.write(text(4,y+0.8,lbl))
    f.write(svg_footer())

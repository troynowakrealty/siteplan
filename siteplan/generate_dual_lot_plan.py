from siteplan.geometry import Point, Size, Rectangle
from siteplan.svg_writer import write_svg
import os

OUTPUT_FILE = "output/siteplan_dual_lot.svg"
os.makedirs("output", exist_ok=True)

LOT_WIDTH = 46
LOT_DEPTH = 124
GAP_BETWEEN_LOTS = 0

def build_lot(x_offset: float, right_setback: float, label_prefix: str):
    shapes = []
    lot = Rectangle(x_offset, 0, LOT_WIDTH, LOT_DEPTH)
    shapes.append(("lot", lot))

    # Front Unit
    front_unit = Rectangle(
        x_offset + (LOT_WIDTH - 33) / 2,
        18,
        33,
        28
    )
    shapes.append((f"{label_prefix} Front Unit", front_unit))

    # ADU / Garage
    adu = Rectangle(
        x_offset + (LOT_WIDTH - 30) / 2,
        LOT_DEPTH - 22 - 20,
        30,
        20
    )
    shapes.append((f"{label_prefix} Garage/ADU", adu))

    # Parking
    for i in range(3):
        px = x_offset + i * 9
        py = LOT_DEPTH - 20
        shapes.append((f"{label_prefix} Parking {i+1}", Rectangle(px, py, 9, 20)))

    # Trash Pad
    shapes.append((f"{label_prefix} Trash Pad", Rectangle(x_offset + 3 * 9, LOT_DEPTH - 20, 6, 20)))

    return shapes

def main():
    all_shapes = []
    all_shapes += build_lot(0, right_setback=5, label_prefix="Lot 1")
    all_shapes += build_lot(LOT_WIDTH + GAP_BETWEEN_LOTS, right_setback=8, label_prefix="Lot 2")
    write_svg(all_shapes, OUTPUT_FILE)

if __name__ == "__main__":
    main()

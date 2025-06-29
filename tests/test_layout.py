import pytest

from siteplan.layout import (
    LotSpec,
    BuildingSpec,
    compute_layout,
    Rectangle,
)


def test_compute_layout_basic():
    lot = LotSpec(
        width=50, depth=100, front_setback=25, rear_setback=10, side_setback=5
    )
    duplex = BuildingSpec(width=30, depth=40)
    adu = BuildingSpec(width=20, depth=20)

    layout = compute_layout(lot, duplex, adu)

    assert layout.duplex == Rectangle(5, 25, 30, 40)
    assert layout.adu == Rectangle(25, 70, 20, 20)
    assert layout.parking[0] == Rectangle(5, 5, 15, 20)
    assert layout.parking[1] == Rectangle(20, 5, 15, 20)

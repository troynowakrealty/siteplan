import os

import layout


def test_layout_positions():
    positions = layout.layout_positions()
    duplex = positions["duplex"]
    adu = positions["adu"]
    # ADU should be to the right of duplex with spacing of 10ft (100px)
    assert adu[0] - (duplex[0] + duplex[2]) == layout.ft_to_px(layout.SPACING)


def test_generate_svg_file_output(tmp_path):
    out_file = tmp_path / "plan.svg"
    layout.generate_svg(str(out_file))
    assert out_file.exists()

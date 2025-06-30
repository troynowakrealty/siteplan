from pathlib import Path

from siteplan.geometry import Rectangle
from siteplan.layout import Layout


def test_export_svg_custom_font(tmp_path: Path):
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 10, 10))
    out_file = tmp_path / "plan.svg"
    layout.export_svg(out_file, font_size=20)
    content = out_file.read_text()
    assert "font-size='20'" in content

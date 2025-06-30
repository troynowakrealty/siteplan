from pathlib import Path

from siteplan.geometry import Rectangle
from siteplan.layout import Layout


def test_svg_with_grid(tmp_path: Path):
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 100, 50))
    out_file = tmp_path / "plan.svg"
    layout.export_svg(out_file)
    content = out_file.read_text()
    assert "<line" in content  # gridlines
    assert "<text" in content  # dimension label
    assert "stroke-dasharray='4'" in content  # property boundary
    assert "<polygon" in content  # arrow heads

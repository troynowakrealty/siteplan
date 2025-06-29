from pathlib import Path

from siteplan.geometry import Rectangle
from siteplan.layout import Layout


def test_layout_export(tmp_path: Path):
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 10, 10))
    out_file = tmp_path / "plan.svg"
    layout.export_svg(out_file)
    assert out_file.exists()
    content = out_file.read_text()
    assert "<rect" in content
    assert "</svg>" in content

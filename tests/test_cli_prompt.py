from pathlib import Path
import subprocess
import sys

from siteplan.geometry import Rectangle
from siteplan.layout import Layout


def test_cli_with_prompt(tmp_path: Path):
    out_file = tmp_path / "plan.svg"
    cmd = [
        sys.executable,
        "-m",
        "siteplan.cli",
        str(out_file),
        "--prompt",
        "place house 10x10 at 0,0",
    ]
    subprocess.check_call(cmd)
    assert out_file.exists()
    content = out_file.read_text()
    assert "<rect" in content


def test_cli_append_prompt(tmp_path: Path):
    layout = Layout()
    layout.add_shape(Rectangle(0, 0, 10, 10))
    layout_file = tmp_path / "layout.json"
    layout.save(layout_file)

    out_file = tmp_path / "plan.svg"
    cmd = [
        sys.executable,
        "-m",
        "siteplan.cli",
        str(out_file),
        "--load",
        str(layout_file),
        "--append-prompt",
        "place garage 5x5 at 20,0",
    ]
    subprocess.check_call(cmd)
    assert out_file.exists()
    content = out_file.read_text()
    assert content.count("<rect") == 2

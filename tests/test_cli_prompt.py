from pathlib import Path
import subprocess
import sys


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

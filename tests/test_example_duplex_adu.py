from pathlib import Path
import importlib


def test_example_runs(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    # import module after changing directory so output is in tmp_path
    module = importlib.import_module("examples.duplex_adu")
    module.main()
    svg = Path("output/examples/duplex_adu.svg")
    assert svg.exists()
    content = svg.read_text()
    assert "<rect" in content

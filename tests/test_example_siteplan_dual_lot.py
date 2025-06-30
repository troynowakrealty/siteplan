from pathlib import Path
import importlib


def test_example_siteplan_dual_lot(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    module = importlib.import_module("examples.siteplan_dual_lot")
    module.main()
    svg = Path("output/siteplan_dual_lot.svg")
    assert svg.exists()
    content = svg.read_text()
    # At least ten rectangles should be drawn for lots and features
    assert content.count("<rect") >= 10
    # No text labels should appear in the output
    assert "<text" not in content

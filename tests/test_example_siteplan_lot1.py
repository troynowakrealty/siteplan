from pathlib import Path
import importlib


def test_example_siteplan_lot1(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    module = importlib.import_module("examples.siteplan_lot1")
    module.main()
    svg = Path("output/siteplan_lot1.svg")
    assert svg.exists()
    content = svg.read_text()
    assert "<rect" in content

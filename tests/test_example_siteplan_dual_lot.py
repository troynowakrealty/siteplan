from pathlib import Path
import importlib


def test_example_siteplan_dual_lot(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    module = importlib.import_module("examples.siteplan_dual_lot")
    module.main()
    svg = Path("output/siteplan_dual_lot.svg")
    assert svg.exists()
    content = svg.read_text()
    assert "<rect" in content
    assert "Front Setback" in content
    assert "Front Duplex" in content
    assert "Porch A" in content

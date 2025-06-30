from pathlib import Path
import importlib


def test_example_siteplan_dual_lot(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    module = importlib.import_module("examples.siteplan_dual_lot")
    module.main()
    svg = Path("output/siteplan_dual_lot.svg")
    assert svg.exists()
    content = svg.read_text()
    # Ensure basic shapes and dimension labels exist
    assert content.count("<rect") >= 10
    assert "Lot 2 Width" in content
    assert "Lot 1 Width" in content

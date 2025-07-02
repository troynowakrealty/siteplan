from pathlib import Path
import importlib


def test_generate_simple_dual_lot(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    module = importlib.import_module("siteplan.generate_simple_dual_lot")
    shapes = module.main()
    svg = Path("output/siteplan_dual_lot.svg")
    assert svg.exists()
    content = svg.read_text()
    assert "Front Unit" in content
    assert any("Parking" in label for label, _ in shapes)

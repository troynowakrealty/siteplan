1. **Initialize Python package structure** - Create `pyproject.toml`, configure black and flake8, and add an empty `siteplan` package.
   - Files: `pyproject.toml`, `.flake8`, `siteplan/__init__.py`
2. **Implement geometry and SVG utilities** - Add `geometry.py` with rectangle primitives and `svg_writer.py` for basic SVG generation.
   - Files: `siteplan/geometry.py`, `siteplan/svg_writer.py`
3. **Create duplex + ADU layout generator** - Add `layout.py` to compute building footprints and positions using geometry primitives.
   - Files: `siteplan/layout.py`
4. **Add CLI for SVG site plan generation** - Provide `cli.py` exposing command-line interface to render the duplex + ADU site plan.
   - Files: `siteplan/cli.py`
5. **Write tests and update documentation** - Add pytest-based tests for geometry and layout modules and expand README with usage instructions.
   - Files: `tests/test_geometry.py`, `tests/test_layout.py`, `README.md`

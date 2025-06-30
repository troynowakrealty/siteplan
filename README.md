# Siteplan

This project provides a minimal site plan generator that outputs an SVG file.

## Installation

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Running the CLI

Generate a simple site plan SVG:

```bash
python -m siteplan.cli output/siteplan.svg
```

You can also provide prompt instructions:

```bash
python -m siteplan.cli output/siteplan.svg --prompt "place house 20x30 at 0,0"
```

Or read the prompt from a file using the `@` prefix:

```bash
python -m siteplan.cli output/siteplan.svg --prompt @prompt.txt
```

The output SVG will be written to the path provided (default `output/siteplan.svg`).

## Running Tests

Execute the automated tests with `pytest`:

```bash
pytest
```

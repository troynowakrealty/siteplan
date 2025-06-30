# Siteplan

This project provides a minimal site plan generator that outputs an SVG file.

## Installation

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

Interactive features such as the checklist mode use the optional `pexpect`
package. Install it separately if you plan to run those features or their
corresponding tests:

```bash
pip install pexpect
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

### Interactive Checklist Mode

Use `--interactive-checklist` to step through shape placement interactively. The
CLI will prompt you for each rectangle and confirm before writing to the output
SVG:

```bash
python -m siteplan.cli output/siteplan.svg --interactive-checklist
```

### Adjusting Font Size

To scale the dimension labels, pass `--font-scale` with the desired multiplier
(for example, `--font-scale 1.5` for 50% larger text):

```bash
python -m siteplan.cli output/siteplan.svg --font-scale 1.5
```

### Appending to an Existing Layout

You can load a previously saved layout and add more shapes using
`--append-prompt`. The layout file can be JSON or a Python pickle created with
the `Layout.save` method.

```bash
python -m siteplan.cli output/siteplan.svg \
    --load layout.json \
    --append-prompt "place shed 10x10 at 50,0"
```

After applying the appended instructions the SVG at `output/siteplan.svg` will
be overwritten with the updated drawing.

The output SVG will be written to the path provided (default `output/siteplan.svg`).

## Running Tests

Execute the automated tests with `pytest`:

```bash
pytest
```

## Examples

Generate a duplex and ADU layout from a multi-line prompt:

```bash
python examples/duplex_adu.py
```

The resulting SVG will be written to `output/examples/duplex_adu.svg`.

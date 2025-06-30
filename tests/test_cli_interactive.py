import sys
from pathlib import Path

import pytest

pexpect = pytest.importorskip("pexpect")


def test_cli_interactive(tmp_path: Path):
    """Run the CLI inside a Python REPL using pexpect and verify output."""
    child = pexpect.spawn(sys.executable, ["-i"], cwd=tmp_path, encoding="utf-8")
    child.expect(">>>")
    child.sendline("from siteplan.cli import main")
    child.expect(">>>")
    child.sendline("main('plan.svg')")
    child.expect(">>>", timeout=10)
    child.sendline("exit()")
    child.expect(pexpect.EOF)
    assert (tmp_path / "plan.svg").exists()

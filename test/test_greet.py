""" Greet tests on the CLI """
from click.testing import CliRunner

from example.greet import greet


def test_greet_cli():
    """Case with only time zone"""
    runner = CliRunner()
    result = runner.invoke(greet, ["Europe/Istanbul"])
    assert result.exit_code == 0
    assert "Hello, Istanbul!" in result.output

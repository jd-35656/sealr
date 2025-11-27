# SPDX-FileCopyrightText: 2025-present jd-35656 <jitesh.sahani@outlook.com>
#
# SPDX-License-Identifier: MIT

from click.testing import CliRunner

from sealr.cli import sealr


def test_sealr_command():
    """Test basic sealr command execution."""
    runner = CliRunner()
    result = runner.invoke(sealr)

    assert result.exit_code == 0
    assert "Hello dreamers!" in result.output


def test_sealr_version():
    """Test sealr version option."""
    runner = CliRunner()
    result = runner.invoke(sealr, ["--version"])

    assert result.exit_code == 0
    assert "sealr" in result.output


def test_sealr_help():
    """Test sealr help option."""
    runner = CliRunner()
    result = runner.invoke(sealr, ["--help"])

    assert result.exit_code == 0
    assert "Usage:" in result.output

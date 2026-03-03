import pytest


import cge


def test_jarbin_toolkit_attributes(
    ) -> None:
    assert hasattr(cge, "Action")
    assert hasattr(cge, "Config")
    assert hasattr(cge, "Console")
    assert hasattr(cge, "Error")
    assert hasattr(cge, "Log")
    assert hasattr(cge, "Time")
    assert hasattr(cge, "get_info")
    assert hasattr(cge, "benchmark")
    assert hasattr(cge, "fail")
    assert hasattr(cge, "text")
    assert hasattr(cge, "IS_TTY")
    assert hasattr(cge, "OS")
    assert hasattr(cge, "TERM")
    assert hasattr(cge, "sleep")
    assert hasattr(cge, "pause")
    assert hasattr(cge, "print")
    assert hasattr(cge, "input")
    assert hasattr(cge, "flush")
    assert hasattr(cge, "stdin")
    assert hasattr(cge, "stdout")
    assert hasattr(cge, "stderr")
    assert hasattr(cge, "critic")
    assert hasattr(cge, "error")
    assert hasattr(cge, "warning")
    assert hasattr(cge, "valid")
    assert hasattr(cge, "debug")
    assert hasattr(cge, "info")
    assert hasattr(cge, "bold")
    assert hasattr(cge, "underline")
    assert hasattr(cge, "color")
    assert hasattr(cge, "up")
    assert hasattr(cge, "down")
    assert hasattr(cge, "left")
    assert hasattr(cge, "right")
    assert hasattr(cge, "clear")
    assert hasattr(cge, "clear_line")

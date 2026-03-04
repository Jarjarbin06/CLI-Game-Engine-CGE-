import pytest


import cge


def test_attributes(
        ) -> None:
    assert hasattr(cge, "get_info")
    assert hasattr(cge, "benchmark")
    assert hasattr(cge, "fail")
    assert hasattr(cge, "text")
    assert hasattr(cge, "IS_TTY")
    assert hasattr(cge, "OS")
    assert hasattr(cge, "TERM")
    assert hasattr(cge, "Sprite")
    assert hasattr(cge, "Data")


def test_get_info(
        ) -> None:

    assert isinstance(cge.get_info(), dict)


def test_benchmark(
        ) -> None:

    result, elapsed = cge.benchmark(lambda x: x + 1, 10)
    assert result == 11
    assert round(elapsed, 0) == 0


def test_fail(
        ) -> None:

    try:
        cge.fail("a fail")

    except cge.Error as e:
        assert "a fail" in str(e)

    else:
        assert False


def test_text(
        ) -> None:

    text = cge.text("this ", "is ", "a ", "text")
    assert str(text) == "this is a text"

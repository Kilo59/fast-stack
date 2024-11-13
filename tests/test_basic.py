import pytest


def test_foo():
    assert "foobar"


if __name__ == "__main__":
    pytest.main([__file__, "-vv"])

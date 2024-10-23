import pytest

def test_foo():
    assert "foobar"

def test_hello():
    from fast_stack.hello import say_hello
    assert say_hello() == "Hellow from fast-stack"


if __name__ == "__main__":
    pytest.main([__file__, "-vv"])
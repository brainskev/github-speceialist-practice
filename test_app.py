from app import greet


def test_greet():
    assert greet("kevin") == "Hello, kevin!"
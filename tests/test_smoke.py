from workspace_app import greet


def test_greet_default() -> None:
    assert greet() == "hello, world"

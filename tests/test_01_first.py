# This is a simple function test in Python using pytest
# The name of the method start with "test_<method_name>"


def test_hello_world():
    hello = "Hello World"
    assert hello.upper() == "HELLO WORLD"


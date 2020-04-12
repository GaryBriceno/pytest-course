# This is a simple class test in Python using pytest
# The name of the class start with "Test<ClassName>"


class TestFirstClass:

    def test_second_test(self):
        hello = "Hello world"
        assert hello.upper() == "HELLO WORLD"

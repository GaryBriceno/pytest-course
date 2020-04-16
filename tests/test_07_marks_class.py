# This file has examples about how Pytest use the marks in the class
# The mark that we use is: @pytest.mark.test_class
import pytest


@pytest.mark.test_class
class TestClass:

    def test_startup(self):
        pass

    def test_startup_and_more(self):
        pass

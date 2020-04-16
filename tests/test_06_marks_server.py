# This file has examples about how Pytest use the marks in the methods
# The mark that we use is: @pytest.mark.webtest
import pytest


@pytest.mark.webtest
def test_send_http():
    pass


def test_something_quick():
    pass


def test_another():
    pass


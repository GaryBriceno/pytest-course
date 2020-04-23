# In this file we work with the Pytest marks:
# - skip(): not run the test
# - skipif(): not run the test if the condition if true
# - xfail(): not reported the error detail if the test fail
import pytest
import sys

my_mark = pytest.mark.skipif(sys.version_info > (3,0),
                             reason="The version of Python is more than 3.0")


@pytest.mark.skip(reason="SKip for now")
def test_mark_for_skip():
    raise Exception


def test_without_skip():
    pass


@my_mark
def test_mark_for_skipif():
    pass


@pytest.mark.xfail()
def test_mark_for_xfail():
    raise Exception

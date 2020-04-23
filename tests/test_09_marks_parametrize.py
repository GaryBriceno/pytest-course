# In this file, we use the mark parametrize to do multiples test
# - pytest.mark.parametrize()
import pytest


def fibonacci(n):
    # 0 1 1 2 3 ....
    old, new = 0, 1
    for _ in range(n):
        old, new = new , old + new
    return old


@pytest.mark.parametrize("test_input, expected",
                         [("3+5", 8),
                          ("9-5", 4),
                          ("9*3", 27)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("n, result",
                         [(0, 0),
                          (1, 1),
                          (2, 1),
                          (3, 2),
                          (4, 3),
                          (5, 5)
                          ])
def test_fibonacci(n, result):
    assert fibonacci(n) == result
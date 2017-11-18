"""Grep-like search in python data strucures, with IPython magic support.
"""

__version__ = 0.1
__license__ = "BSD (3-clause)"


import re


def grep(pat, *iters, values=True):
    """

    """

    rpat = re.compile(pat)

    for ds in iters:
        rpat.    




def test_string():
    assert grep('hello', 'hello world') == 'hello'

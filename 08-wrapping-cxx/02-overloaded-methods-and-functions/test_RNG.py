# -*- coding: utf-8 -*-
"""
pytest unit test file for RNG Cython class
"""
from RNG import RNG


def test_ctor1():
    r = RNG(42)
    assert isinstance(r, RNG)
    assert 0.37454011439684315 == r.rand()


def test_ctor2():
    r2 = RNG(range(30, 40))
    assert isinstance(r2, RNG)
    assert 0.04691027990703245 == r2.rand()
    assert 2626217183 == r2.randint()


def test_call_operator():
    r = RNG(10)
    assert 0.7713206433158649 == r()

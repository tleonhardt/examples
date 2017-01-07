# -*- coding: utf-8 -*-
"""
pytest unit test file for RNG Cython class
"""
from RNG import RNG


def test_ctor():
    r = RNG(42)
    assert isinstance(r, RNG)


def test_seed():
    r = RNG(42)
    assert 1608637542 == r.randint()
    assert 3421126067 == r.randint()
    assert 0.9507143117838339 == r.rand()
    assert 0.1834347877147223 == r.rand()

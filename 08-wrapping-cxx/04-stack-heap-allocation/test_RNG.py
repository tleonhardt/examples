# -*- coding: utf-8 -*-
"""
pytest unit test file for RNG Cython code
"""
from RNG import make_random_list


def test_make_random_list():
    rnd_lst = make_random_list(42, 2)
    assert [1608637542, 3421126067] == rnd_lst

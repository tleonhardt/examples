# -*- coding: utf-8 -*-
"""
pytest unit test file for periodic_table.pyx and std_sort_vector.pyx
"""

import periodic_table as pt
from std_sort_vector import sort_list


def test_manual_pt():
    periodic = pt.periodic_table_orig()
    assert periodic[b'H'] == 1
    assert periodic[b'He'] == 2


def test_dict_pt():
    periodic = pt.periodic_table()
    assert periodic[b'H'] == 1
    assert periodic[b'He'] == 2
    assert periodic[b'Li'] == 3


def test_sort():
    a = [5,3,4,2,0,1]
    b = a.copy()
    a.sort()
    assert a == sort_list(b)
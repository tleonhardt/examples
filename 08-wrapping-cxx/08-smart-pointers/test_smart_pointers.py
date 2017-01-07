# -*- coding: utf-8 -*-
"""
pytest unit test file for periodic_table.pyx and std_sort_vector.pyx
"""

from hist_sum import hist_sum


def test_hist_sum():
    assert 4.5 == hist_sum(range(10))
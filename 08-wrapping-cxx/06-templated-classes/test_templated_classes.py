# -*- coding: utf-8 -*-
"""
pytest unit test file for templated_classes.pyx
"""

import templated_classes as tc


def test_rotate_list():
    assert [5, 6, 7, 8, 9, 0, 1, 2, 3, 4] == tc.rotate_list(list(range(10)), 5)
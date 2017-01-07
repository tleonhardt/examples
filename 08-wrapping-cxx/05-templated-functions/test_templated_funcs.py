# -*- coding: utf-8 -*-
"""
pytest unit test file for templated_funcs.pyx
"""
import templated_funcs as tf


def test_min_long():
    assert tf.min(5, 7) == 5


def test_min_double():
    assert tf.min(2.3, 2.1) == 2.1


def test_max_long():
    assert max(23, 42) == 42


def test_max_double():
    assert max(3.14159, 2.7) == 3.14159
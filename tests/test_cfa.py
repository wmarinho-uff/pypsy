# coding=utf-8
from __future__ import print_function, division, unicode_literals
import numpy as np
from psy import cfa


def test_cfa():
    lam = np.array([
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
    ])
    data = np.loadtxt('data/ex5.6.dat')
    cfa(data, lam)
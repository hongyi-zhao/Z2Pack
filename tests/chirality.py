#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    12.04.2015 22:06:14 CEST
# File:    chirality.py

from common import *

import numpy as np

pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)
pauli_vector = list([pauli_x, pauli_y, pauli_z])

class ChiralityTestCase(CommonTestCase):

    def test_positive(self):
        def hamilton(k):
            res = np.zeros((2, 2), dtype=complex)
            for kval, p_mat in zip(k, pauli_vector):
                res += kval * p_mat
            return res
        system = z2pack.em.System(hamilton)
        surface = system.surface(z2pack.shapes.Sphere([0., 0., 0.], 0.01), pickle_file=None)
        surface.wcc_calc(verbose=False)

        res = {'t_par': [0.0, 0.10000000000000001, 0.20000000000000001, 0.30000000000000004, 0.40000000000000002, 0.5, 0.60000000000000009, 0.70000000000000007, 0.80000000000000004, 0.90000000000000002, 1.0], 'wcc': [[0.0], [0.022998948596837838], [0.090891756468587326], [0.19965786212300812], [0.34073312742650147], [0.49999999999999989], [0.6592668725734987], [0.80034213787699182], [0.90910824353141262], [0.97700105140316218], [1.0]], 'lambda_': [array([[ 1.+0.j]]), array([[ 0.98957707-0.14400425j]]), array([[ 0.84131241-0.54054919j]]), array([[ 0.31106078-0.95039002j]]), array([[-0.53971039-0.84185076j]]), array([[-1. -7.21644966e-16j]]), array([[-0.53971039+0.84185076j]]), array([[ 0.31106078+0.95039002j]]), array([[ 0.84131241+0.54054919j]]), array([[ 0.98957707+0.14400425j]]), array([[ 1. +2.20384171e-32j]])], 'kpt': [[0.0, 0.0, -0.01], [0.0030901699437494742, 0.0, -0.0095105651629515363], [0.0058778525229247315, 0.0, -0.0080901699437494739], [0.0080901699437494739, 0.0, -0.0058778525229247307], [0.0095105651629515363, 0.0, -0.0030901699437494747], [0.01, 0.0, -6.123233995736766e-19], [0.0095105651629515363, 0.0, 0.0030901699437494755], [0.0080901699437494739, 0.0, 0.0058778525229247307], [0.0058778525229247324, 0.0, 0.0080901699437494739], [0.0030901699437494751, 0.0, 0.0095105651629515363], [1.2246467991473532e-18, 0.0, 0.01]], 'gap': [0.5, 0.52299894859683782, 0.59089175646858738, 0.69965786212300807, 0.84073312742650153, 0.99999999999999989, 0.1592668725734987, 0.30034213787699171, 0.40910824353141262, 0.47700105140316218, 0.5]}

        self.assertFullAlmostEqual(res, surface.get_res())

    def test_negative(self):
        def hamilton(k):
            k[2] = -k[2]
            res = np.zeros((2, 2), dtype=complex)
            for kval, p_mat in zip(k, pauli_vector):
                res += kval * p_mat
            return res
        system = z2pack.em.System(hamilton)
        surface = system.surface(z2pack.shapes.Sphere([0., 0., 0.], 0.04), pickle_file=None)
        surface.wcc_calc(verbose=False)

        res = {'t_par': [0.0, 0.10000000000000001, 0.20000000000000001, 0.30000000000000004, 0.40000000000000002, 0.5, 0.60000000000000009, 0.70000000000000007, 0.80000000000000004, 0.90000000000000002, 1.0], 'wcc': [[0.0], [0.97700105140316218], [0.90910824353141262], [0.80034213787699182], [0.65926687257349847], [0.5], [0.34073312742650147], [0.19965786212300812], [0.09089175646858734], [0.022998948596837845], [0.0]], 'lambda_': [array([[ 1.+0.j]]), array([[ 0.98957707+0.14400425j]]), array([[ 0.84131241+0.54054919j]]), array([[ 0.31106078+0.95039002j]]), array([[-0.53971039+0.84185076j]]), array([[-1. -5.55111512e-17j]]), array([[-0.53971039-0.84185076j]]), array([[ 0.31106078-0.95039002j]]), array([[ 0.84131241-0.54054919j]]), array([[ 0.98957707-0.14400425j]]), array([[ 1.+0.j]])], 'kpt': [[0.0, 0.0, -0.040000000000000001], [0.012360679774997897, 0.0, -0.038042260651806145], [0.023511410091698926, 0.0, -0.032360679774997896], [0.032360679774997896, 0.0, -0.023511410091698923], [0.038042260651806145, 0.0, -0.012360679774997899], [0.040000000000000001, 0.0, -2.4492935982947064e-18], [0.038042260651806145, 0.0, 0.012360679774997902], [0.032360679774997896, 0.0, 0.023511410091698923], [0.02351141009169893, 0.0, 0.032360679774997896], [0.0123606797749979, 0.0, 0.038042260651806145], [4.8985871965894128e-18, 0.0, 0.040000000000000001]], 'gap': [0.5, 0.47700105140316218, 0.40910824353141262, 0.30034213787699171, 0.15926687257349847, 0.0, 0.84073312742650153, 0.69965786212300807, 0.59089175646858738, 0.52299894859683782, 0.5]}

        self.assertFullAlmostEqual(res, surface.get_res())


if __name__ == "__main__":
    unittest.main()    

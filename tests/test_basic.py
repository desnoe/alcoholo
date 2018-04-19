# -*- coding: utf-8 -*-

from .context import alcoholo

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    # Table I
    def test_rho_p_t(self):
        self.assertEqual(round(alcoholo.tables.rho_p_t(30 / 100, -20.0), 2), 974.91)
        self.assertEqual(round(alcoholo.tables.rho_p_t(10 / 100, 0.0), 2), 984.75)
        self.assertEqual(round(alcoholo.tables.rho_p_t(100 / 100, 0.0), 2), 806.22)
        self.assertEqual(round(alcoholo.tables.rho_p_t(50 / 100, 20.0), 2), 913.77)

    # Table VI
    def test_p_rho_t(self):
        self.assertEqual(round(100 * alcoholo.tables.p_rho_t(974.91, -20.0), 2), 30.00)
        self.assertEqual(round(100 * alcoholo.tables.p_rho_t(984.75, 0.0), 2), 10.00)
        self.assertEqual(round(100 * alcoholo.tables.p_rho_t(806.22, 0.0), 2), 100.00)
        self.assertEqual(round(100 * alcoholo.tables.p_rho_t(913.77, 20.0), 2), 50.00)

    # Table VII
    def test_q_rho_t(self):
        self.assertEqual(round(alcoholo.tables.q_rho_t(974.91, -20.0), 2), round(alcoholo.tables.q_p(30.00 / 100), 2))
        self.assertEqual(round(alcoholo.tables.q_rho_t(984.75, 0.0), 2), round(alcoholo.tables.q_p(10.00 / 100), 2))
        self.assertEqual(round(alcoholo.tables.q_rho_t(806.22, 0.0), 2), round(alcoholo.tables.q_p(100.00 / 100), 2))
        self.assertEqual(round(alcoholo.tables.q_rho_t(913.77, 20.0), 2), round(alcoholo.tables.q_p(50.00 / 100), 2))

    # Table VIIIa
    def test_p_p_t(self):
        self.assertEqual(round(100 * alcoholo.tables.p_p_t(17.5 / 100, -10.0), 1), 27.6)
        self.assertEqual(round(100 * alcoholo.tables.p_p_t(68.0 / 100, 0.0), 1), 74.8)
        self.assertEqual(round(100 * alcoholo.tables.p_p_t(57.0 / 100, 6.0), 1), 61.8)
        self.assertEqual(round(100 * alcoholo.tables.p_p_t(1.5 / 100, 12.0), 1), 2.1)
        self.assertEqual(round(100 * alcoholo.tables.p_p_t(67.0 / 100, 35.0), 1), 61.7)

    # Table VIIIb
    def test_q_q_t(self):
        self.assertEqual(round(100 * alcoholo.tables.q_q_t(17.5 / 100, -10.0), 1), 26.0)
        self.assertEqual(round(100 * alcoholo.tables.q_q_t(68.0 / 100, 0.0), 1), 74.3)
        self.assertEqual(round(100 * alcoholo.tables.q_q_t(57.0 / 100, 6.0), 1), 61.9)
        self.assertEqual(round(100 * alcoholo.tables.q_q_t(1.5 / 100, 12.0), 1), 2.2)
        self.assertEqual(round(100 * alcoholo.tables.q_q_t(67.0 / 100, 35.0), 1), 61.8)


if __name__ == '__main__':
    unittest.main()

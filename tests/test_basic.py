# -*- coding: utf-8 -*-

from .context import alcoholo

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    # Table I
    def test_rho_p_t(self):
        self.assertEqual(round(alcoholo.tables.rho_p_t(30.0 / 100, -20.0), 2), 974.91)
        self.assertEqual(round(alcoholo.tables.rho_p_t(10.0 / 100, 0.0), 2), 984.75)
        self.assertEqual(round(alcoholo.tables.rho_p_t(100.0 / 100, 0.0), 2), 806.22)
        self.assertEqual(round(alcoholo.tables.rho_p_t(50.0 / 100, 20.0), 2), 913.77)

    # Table II
    def test_rho_q_t(self):
        self.assertEqual(round(alcoholo.tables.rho_q_t(36.0 / 100, -20.0), 2), 975.08)
        self.assertEqual(round(alcoholo.tables.rho_q_t(10.0 / 100, 0.0), 2), 987.12)
        self.assertEqual(round(alcoholo.tables.rho_q_t(100.0 / 100, 0.0), 2), 806.22)
        self.assertEqual(round(alcoholo.tables.rho_q_t(50.0 / 100, 20.0), 2), 930.14)

    # Table IIIa
    def test_rho20_p(self):
        self.assertEqual(round(alcoholo.tables.rho20_p(20.0 / 100), 2), 968.61)
        self.assertEqual(round(alcoholo.tables.rho20_p(50.0 / 100), 2), 913.77)

    # Table IIIb
    def test_q_p(self):
        self.assertEqual(round(100 * alcoholo.tables.q_p(10.0 / 100), 2), 12.44)
        self.assertEqual(round(100 * alcoholo.tables.q_p(30.0 / 100), 2), 36.25)
        self.assertEqual(round(100 * alcoholo.tables.q_p(50.0 / 100), 2), 57.89)
        self.assertEqual(round(100 * alcoholo.tables.q_p(70.0 / 100), 2), 76.95)

    # Table IVa
    def test_rho20_q(self):
        self.assertEqual(round(alcoholo.tables.rho20_q(20.0 / 100), 2), 973.56)
        self.assertEqual(round(alcoholo.tables.rho20_q(50.0 / 100), 2), 930.14)

    # Table IVb
    def test_p_q(self):
        self.assertEqual(round(100 * alcoholo.tables.p_q(10.0 / 100), 2), 8.01)
        self.assertEqual(round(100 * alcoholo.tables.p_q(30.0 / 100), 2), 24.61)
        self.assertEqual(round(100 * alcoholo.tables.p_q(50.0 / 100), 2), 42.43)
        self.assertEqual(round(100 * alcoholo.tables.p_q(70.0 / 100), 2), 62.39)

    # Table Va
    def test_p_rho20(self):
        self.assertEqual(round(100 * alcoholo.tables.p_rho20(790.0), 2), 99.76)
        self.assertEqual(round(100 * alcoholo.tables.p_rho20(800.0), 2), 96.44)
        self.assertEqual(round(100 * alcoholo.tables.p_rho20(900.0), 2), 56.12)
        self.assertEqual(round(100 * alcoholo.tables.p_rho20(950.0), 2), 32.20)
        self.assertEqual(round(100 * alcoholo.tables.p_rho20(970.0), 2), 18.95)
        self.assertEqual(round(100 * alcoholo.tables.p_rho20(990.0), 2), 4.62)

    # Table Vb
    def test_q_rho20(self):
        self.assertEqual(round(100 * alcoholo.tables.q_rho20(790.0), 2), 99.85)
        self.assertEqual(round(100 * alcoholo.tables.q_rho20(800.0), 2), 97.75)
        self.assertEqual(round(100 * alcoholo.tables.q_rho20(900.0), 2), 64.00)
        self.assertEqual(round(100 * alcoholo.tables.q_rho20(950.0), 2), 38.76)
        self.assertEqual(round(100 * alcoholo.tables.q_rho20(970.0), 2), 23.29)
        self.assertEqual(round(100 * alcoholo.tables.q_rho20(990.0), 2), 5.79)

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

    # Table IXa
    # TODO

    # Table IXb
    # TODO

    # Table Xa
    # TODO

    # Table Xb
    # TODO

    # Table XIa
    def test_v_p_t_100l(self):
        self.assertEqual(round(alcoholo.tables.v_p_t_100l(0.0 / 100, 0.0), 1), 0.0)
        self.assertEqual(round(alcoholo.tables.v_p_t_100l(100.0 / 100, 20.0), 1), 100.0)

    # Table XIb
    def test_v_q_t_100l(self):
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(0.0 / 100, 0.0), 1), 0.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(10.0 / 100, 20.0), 1), 10.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(20.0 / 100, 20.0), 1), 20.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(30.0 / 100, 20.0), 1), 30.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(40.0 / 100, 20.0), 1), 40.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(50.0 / 100, 20.0), 1), 50.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(60.0 / 100, 20.0), 1), 60.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(70.0 / 100, 20.0), 1), 70.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(80.0 / 100, 20.0), 1), 80.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(90.0 / 100, 20.0), 1), 90.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100l(100.0 / 100, 20.0), 1), 100.0)

    # Table XIIa
    def test_v_p_t_100kg(self):
        self.assertEqual(round(alcoholo.tables.v_p_t_100kg(0.0 / 100, 0.0), 1), 0.0)
        self.assertEqual(round(alcoholo.tables.v_p_t_100kg(100.0 / 100, 20.0), 1), 126.9)

    # Table XIIb
    def test_v_q_t_100kg(self):
        self.assertEqual(round(alcoholo.tables.v_q_t_100kg(0.0 / 100, 0.0), 1), 0.0)
        self.assertEqual(round(alcoholo.tables.v_q_t_100kg(100.0 / 100, 20.0), 1), 126.9)


if __name__ == '__main__':
    unittest.main()

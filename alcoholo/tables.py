# -*- coding: utf-8 -*-

"""
INTERNATIONAL ALCOHOLOMETRIC TABLES
"""

from scipy import optimize


# Table I
def rho_p_t(p, t):
    """
    Table I gives the density of a mixture as a function of the temperature in °C, from — 20 °C to + 40 °C, and of the
    alcoholic strength by mass from the minimum permissible value and 100%, this minimum value corresponding to the
    freezing of the mixture for the temperature considered.

    :param p: alcoholic strength by mass in %
    :type p: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: density of a mixture of water and ethanol in kg/m3
    :rtype: float
    """
    ak = [0] * (1 + 12)

    ak[1] = 9.982012300E2
    ak[2] = -1.929769495E2
    ak[3] = 3.891238958E2
    ak[4] = -1.668103923E3
    ak[5] = 1.352215441E4
    ak[6] = -8.829278388E4
    ak[7] = 3.062874042E5
    ak[8] = -6.138381234E5
    ak[9] = 7.470172998E5
    ak[10] = -5.478461354E5
    ak[11] = 2.234460334E5
    ak[12] = -3.903285426E4

    bk = [0] * (1 + 6)

    bk[1] = -2.0618513E-1
    bk[2] = -5.2682542E-3
    bk[3] = 3.6130013E-5
    bk[4] = -3.8957702E-7
    bk[5] = 7.1693540E-9
    bk[6] = -9.9739231E-11

    c1k = [0] * (1 + 11)

    c1k[1] = 1.693443461530087E-1
    c1k[2] = -1.046914743455169E1
    c1k[3] = 7.196353469546523E1
    c1k[4] = -7.047478054272792E2
    c1k[5] = 3.924090430035045E3
    c1k[6] = -1.210164659068747E4
    c1k[7] = 2.248646550400788E4
    c1k[8] = -2.605562982188164E4
    c1k[9] = 1.852373922069467E4
    c1k[10] = -7.420201433430137E3
    c1k[11] = 1.285617841998974E3

    c2k = [0] * (1 + 10)

    c2k[1] = -1.193013005057010E-2
    c2k[2] = 2.517399633803461E-1
    c2k[3] = -2.170575700536993
    c2k[4] = 1.353034988843029E1
    c2k[5] = -5.029988758547014E1
    c2k[6] = 1.096355666577570E2
    c2k[7] = -1.422753946421155E2
    c2k[8] = 1.080435942856230E2
    c2k[9] = -4.414153236817392E1
    c2k[10] = 7.442971530188783

    c3k = [0] * (1 + 9)

    c3k[1] = -6.802995733503803E-4
    c3k[2] = 1.876837790289664E-2
    c3k[3] = -2.002561813734156E-1
    c3k[4] = 1.022992966719220
    c3k[5] = -2.895696483903638
    c3k[6] = 4.810060584300675
    c3k[7] = -4.672147440794683
    c3k[8] = 2.458043105903461
    c3k[9] = -5.411227621436812E-1

    c4k = [0] * (1 + 4)

    c4k[1] = 4.075376675622027E-6
    c4k[2] = -8.763058573471110E-6
    c4k[3] = 6.515031360099368E-6
    c4k[4] = -1.515784836987210E-6

    c5k = [0] * (1 + 2)

    c5k[1] = -2.788074354782409E-8
    c5k[2] = 1.345612883493354E-8

    return (sum([ak[k] * (p ** (k - 1)) for k in range(1, len(ak))])
            + sum([bk[k] * (t - 20) ** k for k in range(1, len(bk))])
            + sum([c1k[k] * (p ** k) * ((t - 20) ** 1) for k in range(1, len(c1k))])
            + sum([c2k[k] * (p ** k) * ((t - 20) ** 2) for k in range(1, len(c2k))])
            + sum([c3k[k] * (p ** k) * ((t - 20) ** 3) for k in range(1, len(c3k))])
            + sum([c4k[k] * (p ** k) * ((t - 20) ** 4) for k in range(1, len(c4k))])
            + sum([c5k[k] * (p ** k) * ((t - 20) ** 5) for k in range(1, len(c5k))]))


# Table II
def rho_q_t(q, t):
    """
    Table II gives the density of a mixture as a function of the temperature varying from — 20 °C to + 40 °C
    and of the alcoholic strength by volume varying between the minimum permissible value and 100 %.

    :param q: alcoholic strength by volume in %
    :type q: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: density of a mixture of water and ethanol in kg/m3
    :rtype: float
    """
    return rho_p_t(p_q(q), t)


# Table IIIa
def rho20_p(p):
    """
    Table IIIa gives the density at 20 °C as a function of the alcoholic strength by mass varying between 0 % and
    100 %.

    :param p: alcoholic strength by mass in %
    :type p: float
    :return: density of a mixture of water and ethanol in kg/m3 at 20 °C
    :rtype: float
    """
    return rho_p_t(p, 20.0)


# Table IIIb
def q_p(p):
    """
    Table IIIb gives the alcoholic strength by volume as a function of the alcoholic strength by mass varying between
    0 % and 100 %.

    :param p: alcoholic strength by mass in %
    :type p: float
    :return: alcoholic strength by volume in %
    :rtype: float
    """
    return p * rho_p_t(p, 20.0) / rho_p_t(1, 20.0)


# Table IVa
def rho20_q(q):
    """
    Table IVa gives the density at 20 °C as a function of the alcoholic strength by volume varying between 0 and 100 %.

    :param q: alcoholic strength by volume in %
    :type q: float
    :return: density of a mixture of water and ethanol in kg/m3 at 20 °C
    :rtype: float
    """
    return rho_q_t(q, 20.0)


# Table IVb
def p_q(q):
    """
    Table IVb gives the alcoholic strength by mass as a function of the alcoholic strength by volume varying between
    0 and 100 %.

    :param q: alcoholic strength by volume in %
    :type q: float
    :return: alcoholic strength by mass in %
    :rtype: float
    """

    def q_p_tmp(p):
        # type: (float) -> float
        return q_p(p) - q

    return optimize.brentq(q_p_tmp, 0, 1)


# Table Va
def p_rho20(rho20):
    # type: (float) -> float
    """
    Table Va gives the alcoholic strength by mass as a function of the density at 20 °C varying between 789.3 kg/m3 and
    998.2 kg/m3.

    :param rho20: density of a mixture of water and ethanol in kg/m3 at 20 °C
    :type rho20: float
    :return: alcoholic strength by mass in %
    :rtype: float
    """

    def rho20_p_tmp(p):
        # type: (float, float) -> float
        return rho20_p(p) - rho20

    return optimize.brentq(rho20_p_tmp, 0, 1)


# Table Vb
def q_rho20(rho20):
    # type: (float, float) -> float
    """
    Table Vb gives the alcoholic strength by volume as a function of the density at 20 °C varying between 789.3 kg/m3
    and 998.2 kg/m3.

    :param rho20: density of a mixture of water and ethanol in kg/m3 at 20 °C
    :type rho20: float
    :return: alcoholic strength by volume in %
    :rtype: float
    """

    def rho20_q_tmp(p):
        # type: (float, float) -> float
        return rho20_q(p) - rho20

    return optimize.brentq(rho20_q_tmp, 0, 1)


# Table VI
def p_rho_t(rho, t):
    # type: (float, float) -> float
    """
    Table VI gives the value of the alcoholic strength by mass of a mixture as a function of its Celsius temperature t
    and of its density at this temperature.

    :param rho: density of a mixture of water and ethanol in kg/m3
    :type rho: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by mass in %
    :rtype: float
    """

    def rho_p_t_tmp(p):
        # type: (float, float) -> float
        return rho_p_t(p, t) - rho

    return optimize.brentq(rho_p_t_tmp, 0, 1)


# Table VII
def q_rho_t(rho, t):
    # type: (float, float) -> float
    """
    Table VII gives the alcoholic strength by volume of a mixture as a function of its Celsius temperature t and of its
    density at the same temperature.

    :param rho: density of a mixture of water and ethanol in kg/m3
    :type rho: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by volume in %
    :rtype: float
    """
    return q_p(p_rho_t(rho, t))


# Table VIIIa
def p_p_t(p, t):
    # type: (float, float) -> float
    """
    Table VIIIa gives the value of the alcoholic strength by mass of a mixture at the Celsius temperature t from the
    reading of an alcohometer made of soda lime glass, graduated in units of alcoholic strength by mass (% mass).

    :param p: reading of an alcohometer made of soda lime glass, graduated in units of alcoholic strength by mass
    :type p: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by mass in %
    :rtype: float
    """
    return p_rho20prime_t(rho20_p(p), t)


# Table VIIIb
def q_q_t(q, t):
    # type: (float, float) -> float
    """
    Table VIIIb gives the value of the alcoholic strength by volume of a mixture at the Celsius temperature t from the
    reading of an alcohometer made of soda lime glass, graduated in units of alcoholic strength by volume (% vol).

    :param q: reading of an alcohometer made of soda lime glass, graduated in units of alcoholic strength by volume
    :type q: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by volume in %
    :rtype: float
    """
    return q_rho20prime_t(rho20_q(q), t)


# Table IXa
def p_rho20prime_t(rho20prime, t):
    # type: (float, float) -> float
    """
    Table IXa gives the value of the alcoholic strength by mass of a mixture at the Celsius temperature t from the
    reading of a hydrometer for alcohol in soda lime glass.

    :param rho20prime: reading of a hydrometer for alcohol in soda lime glass
    :type rho20prime: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by mass in %
    :rtype: float
    """
    alpha = 25E-6
    rho_t = rho20prime * (1 - alpha * (t - 20.0))
    return p_rho_t(rho_t, t)


# Table IXb
def q_rho20prime_t(rho20prime, t):
    # type: (float, float) -> float
    """
    Table IXb gives respectively the value of the alcoholic strength by volume of a mixture at the Celsius temperature
    t from the reading of a hydrometer for alcohol in soda lime glass.

    :param rho20prime: reading of a hydrometer for alcohol in soda lime glass
    :type rho20prime: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by volume in %
    :rtype: float
    """
    alpha = 25E-6
    rho_t = rho20prime * (1 - alpha * (t - 20.0))
    return q_rho_t(rho_t, t)


# Table Xa
def p_rho20prime_t_bis(rho20prime, t):
    # type: (float, float) -> float
    """
    Tables Xa gives the value of the alcoholic strength by mass of a mixture at the Celsius temperature t from the
    measurement of the density of this mixture by means of an instrument made of borosilicate glass.

    :param rho20prime: measurement of the density of this mixture by means of an instrument made of borosilicate glass
    :type rho20prime: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by mass in %
    :rtype: float
    """
    alpha = 25E-6
    rhot = rho20prime * (1 - alpha * (t - 20.0))
    return p_rho_t(rhot, t)


# Table Xb
def q_rho20prime_t_bis(rho20prime, t):
    # type: (float, float) -> float
    """
    Tables Xb gives respectively the value of the alcoholic strength by volume of a mixture at the Celsius temperature
    t from the measurement of the density of this mixture by means of an instrument made of borosilicate glass.

    :param rho20prime: measurement of the density of this mixture by means of an instrument made of borosilicate glass
    :type rho20prime: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: alcoholic strength by volume in %
    :rtype: float
    """
    alpha = 25E-6
    rhot = rho20prime * (1 - alpha * (t - 20.0))
    return q_rho_t(rhot, t)


# Table XIa
def v_p_t_100l(p, t):
    # type: (float, float) -> float
    """
    Table XIa gives in dm3 the volume v at 20 °C of pure ethanol contained in 100 dm3 of a mixture of known alcoholic
    strength by mass at the Celsius temperature t, assuming that the volume of 100 dm3 was measured by a container in
    steel calibrated at 20 °C.

    :param p: alcoholic strength by mass in % measured by a container in steel calibrated at 20 °C
    :type p: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: volume v at 20 °C of pure ethanol contained in 100 dm3 of a mixture, in dm3
    :rtype: float
    """
    beta = 36E-6
    return p * (rho_p_t(p, t) / rho20_p(1.0)) * (1 + beta * (t - 20.0)) * 100


# Table XIb
def v_q_t_100l(q, t):
    # type: (float, float) -> float
    """
    Tables XIb gives in dm3 the volume v at 20 °C of pure ethanol contained in 100 dm3 of a mixture of known alcoholic
    strength by volume at the Celsius temperature t, assuming that the volume of 100 dm3 was measured by a container
    in steel calibrated at 20 °C.

    :param q: alcoholic strength by volume in % measured by a container in steel calibrated at 20 °C
    :type q: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: volume v at 20 °C of pure ethanol contained in 100 dm3 of a mixture, in dm3
    :rtype: float
    """
    return v_p_t_100l(p_q(q), t)


# Table XIIa
def v_p_t_100kg(p, t):
    # type: (float, float) -> float
    """
    Table XIIa gives in dm3 the volume v at 20 °C of pure ethanol contained in 100 kg of a mixture of known alcoholic
    strength by mass at the Celsius temperature t. It is assumed that the weighing took place in air whose density was
    1.2 kg/m3, by means of weights characterized by the conventional value of the result of their weighing in air.

    :param p: alcoholic strength by mass in %
    :type p: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: volume v at 20 °C of pure ethanol contained in 100 kg of a mixture, in dm3
    :rtype: float
    """
    return p * (1E3 / rho20_p(1.0)) * (1 - 1.2 * ((1.0 / 8000) - (1 / rho_p_t(p, t)))) * 100


# Table XIIb
def v_q_t_100kg(q, t):
    # type: (float, float) -> float
    """
    Table XIIb gives in dm3 the volume v at 20 °C of pure ethanol contained in 100 kg of a mixture of known alcoholic
    strength by volume at the Celsius temperature t. It is assumed that the weighing took place in air whose density
    was 1.2 kg/m3, by means of weights characterized by the conventional value of the result of their weighing in air.

    :param q: alcoholic strength by volume in %
    :type q: float
    :param t: temperature in °C, from — 20 °C to + 40 °C
    :type t: float
    :return: volume v at 20 °C of pure ethanol contained in 100 kg of a mixture, in dm3
    :rtype: float
    """
    return v_p_t_100kg(p_q(q), t)

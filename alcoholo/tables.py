from scipy import optimize


# Table I
def rho_p_t(p: float, t: float) -> float:
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
def rho_q_t(q: float, t: float) -> float:
    return rho_p_t(p_q(q), t)


# Table IIIa
def rho20_p(p: float) -> float:
    return rho_p_t(p, 20)


# Table IIIb
def q_p(p: float) -> float:
    return p * rho_p_t(p, 20) / rho_p_t(1, 20)


# Table IVa
def rho20_q(q: float) -> float:
    return rho_q_t(q, 20)


# Table IVb
def p_q(q: float) -> float:
    def q_p_tmp(p: float) -> float:
        return q_p(p) - q

    return optimize.brentq(q_p_tmp, 0, 1)


# Table Va
def p_rho20(rho20: float) -> float:
    def rho20_p_tmp(p: float) -> float:
        return rho20_p(p) - rho20

    return optimize.brentq(rho20_p_tmp, 0, 1)


# Table Vb
def q_rho20(rho20: float) -> float:
    def rho20_q_tmp(p: float) -> float:
        return rho20_q(p) - rho20

    return optimize.brentq(rho20_q_tmp, 0, 1)


# Table VI
def p_rho_t(rho: float, t: float) -> float:
    def rho_p_t_tmp(p: float) -> float:
        return rho_p_t(p, t) - rho

    return optimize.brentq(rho_p_t_tmp, 0, 1)


# Table VII
def q_rho_t(rho: float, t: float) -> float:
    return q_p(p_rho_t(rho, t))


# Table VIIIa
def p_p_t(p: float, t: float) -> float:
    return p_rho20prime_t(rho20_p(p), t)


# Table VIIIb
def q_q_t(q: float, t: float) -> float:
    return q_rho20prime_t(rho20_q(q), t)


# Table IXa
def p_rho20prime_t(rho20prime: float, t: float) -> float:
    alpha = 25E-6
    rhot = rho20prime * (1 - alpha * (t - 20))
    return p_rho_t(rhot, t)


# Table IXb
def q_rho20prime_t(rho20prime: float, t: float) -> float:
    alpha = 25E-6
    rhot = rho20prime * (1 - alpha * (t - 20))
    return q_rho_t(rhot, t)


# Table Xa
def p_rho20prime_t_bis(rho20prime: float, t: float) -> float:
    alpha = 25E-6
    rhot = rho20prime * (1 - alpha * (t - 20))
    return p_rho_t(rhot, t)


# Table Xb
def q_rho20prime_t_bis(rho20prime: float, t: float) -> float:
    alpha = 25E-6
    rhot = rho20prime * (1 - alpha * (t - 20))
    return q_rho_t(rhot, t)

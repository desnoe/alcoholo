from scipy import optimize

# Table I
def rhop(p, t):

	Ak = [0]*(1+12)

	Ak[1] = 9.982012300E2
	Ak[2] = -1.929769495E2
	Ak[3] = 3.891238958E2
	Ak[4] = -1.668103923E3
	Ak[5] = 1.352215441E4
	Ak[6] = -8.829278388E4
	Ak[7] = 3.062874042E5
	Ak[8] = -6.138381234E5
	Ak[9] = 7.470172998E5
	Ak[10] = -5.478461354E5
	Ak[11] = 2.234460334E5
	Ak[12] = -3.903285426E4


	Bk = [0]*(1+6)

	Bk[1] = -2.0618513E-1
	Bk[2] = -5.2682542E-3
	Bk[3] = 3.6130013E-5
	Bk[4] = -3.8957702E-7
	Bk[5] = 7.1693540E-9
	Bk[6] = -9.9739231E-11

	C1k = [0]*(1+11)

	C1k[1] = 1.693443461530087E-1
	C1k[2] = -1.046914743455169E1
	C1k[3] = 7.196353469546523E1
	C1k[4] = -7.047478054272792E2
	C1k[5] = 3.924090430035045E3
	C1k[6] = -1.210164659068747E4
	C1k[7] = 2.248646550400788E4
	C1k[8] = -2.605562982188164E4
	C1k[9] = 1.852373922069467E4
	C1k[10] = -7.420201433430137E3
	C1k[11] = 1.285617841998974E3

	C2k = [0]*(1+10)

	C2k[1] = -1.193013005057010E-2
	C2k[2] = 2.517399633803461E-1
	C2k[3] = -2.170575700536993
	C2k[4] = 1.353034988843029E1
	C2k[5] = -5.029988758547014E1
	C2k[6] = 1.096355666577570E2
	C2k[7] = -1.422753946421155E2
	C2k[8] = 1.080435942856230E2
	C2k[9] = -4.414153236817392E1
	C2k[10] = 7.442971530188783

	C3k = [0]*(1+9)

	C3k[1] = -6.802995733503803E-4
	C3k[2] = 1.876837790289664E-2
	C3k[3] = -2.002561813734156E-1
	C3k[4] = 1.022992966719220
	C3k[5] = -2.895696483903638
	C3k[6] = 4.810060584300675
	C3k[7] = -4.672147440794683
	C3k[8] = 2.458043105903461
	C3k[9] = -5.411227621436812E-1

	C4k = [0]*(1+4)

	C4k[1] = 4.075376675622027E-6
	C4k[2] = -8.763058573471110E-6
	C4k[3] = 6.515031360099368E-6
	C4k[4] = -1.515784836987210E-6

	C5k = [0]*(1+2)

	C5k[1] = -2.788074354782409E-8
	C5k[2] = 1.345612883493354E-8

	return sum([Ak[k] * (p ** (k - 1)) for k in range(1,len(Ak))]) \
		   + sum([Bk[k] * (t - 20) ** k for k in range(1, len(Bk))]) \
		   + sum([C1k[k] * (p ** k) * ((t - 20) ** 1) for k in range(1, len(C1k))]) \
		   + sum([C2k[k] * (p ** k) * ((t - 20) ** 2) for k in range(1, len(C2k))]) \
		   + sum([C3k[k] * (p ** k) * ((t - 20) ** 3) for k in range(1, len(C3k))]) \
		   + sum([C4k[k] * (p ** k) * ((t - 20) ** 4) for k in range(1, len(C4k))]) \
		   + sum([C5k[k] * (p ** k) * ((t - 20) ** 5) for k in range(1, len(C5k))])

# Table II
def rhoq(q, t):
	return rhop(pq(q), t)

# Table IIIa
def rho20p(p):
	return rhop(p, 20)

# Table IIIb
def qp(p):
	return p * rhop(p, 20) / rhop(1, 20)

# Table IVa
def rho20q(q):
	return rhoq(q, 20)

# Table IVb
def pq(q):
	def qptmp(p):
		return qp(p) - q
	return optimize.brentq(qptmp, 0, 1)

# Table Va
def prho20(rho20):
	def rho20ptmp(p):
		return rho20p(p) - rho20
	return optimize.brentq(rho20ptmp, 0, 1)

# Table Vb
def qrho20(rho20):
	def rho20qtmp(p):
		return rho20q(p) - rho20
	return optimize.brentq(rho20qtmp, 0, 1)

# adaptation titre volumique en fonction de la température
def q(q20, t):
	p = pq(q20)
	return p * rhop(p, t) / rhop(1, t)


print(round(100*q(0.2,15),2))

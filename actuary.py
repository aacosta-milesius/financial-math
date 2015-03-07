"""
Actuarial defs from Kellison text
"""

import math

def BalanceRemaining(n, t, i):
    # Kellison (6.1) - Prospective
    return AnnuityImmediateA(n - t, i)

def BalanceRemainingR(n, t, i):
    # Kellison (6.2) - Retrospective
    return AnnuityImmediateA(n, i) * (1 + i)**t - AnnuityImmediateS(t, i)

def InterestPaid(n, t, i):
    # Kellison (6.3)
    return 1 - (1 / (1 + i) ** (n - t + 1))

def PrincipalPaid(n, t, i):
    # Kellison (6.4)
    return (1 / (1 + i) ** (n - t + 1))

def SinkingFund(n, i, j):
    # Kellison (6.7)
    return AnnuityImmediateA(n, j) / (1 + (i - j) * AnnuityImmediateA(n, j))

def AnnuityImmediateA(n, i, m = 1):
    # Kellison (3.2)
    return (1 - (1 / (1 + (i / m))) ** (n * m)) / i

def AnnuityImmediateS(n, i, m = 1):
    # Kellison (3.4)
    return ((1 + (i / m)) ** (n * m) - 1) / i

def AnnuityDueA(n, i, m = 1):
    # Kellison
    return ((1 + i) * (1 - (1 / (1 + (i / m))) ** (n * m))) / i

def AnnuityDueS(n, i, m = 1):
    # Kellison
    return ((1 + i) * (-1 + (1 + (i / m)) ** (n * m))) / i

def ContinuousAnnuityA(n, delta, m = 1):
    # Kellison
    return (1 - (1 / (1 + (i / m))) ** (n * m)) / delta

def ContinuousAnnuityS(n, delta, m = 1):
    # Kellison
    return (-1 + (1 + (i / m)) ** (n * m)) / delta

def IncreasingPerpetuityA(i):
    # Kellison
    return (1 + i) / i

def IncreasingAnnuityA(n, i, m = 1):
    # Kellison
    return (AnnuityDueA(n * m, i / m) - n * m * v(i) ** (n * m)) / i

def IncreasingAnnuityS(n, i):
    # Kellison
    return (-1 - n + AnnuityImmediateS(n, i)) / i

def DecreasingAnnuityA(n, i):
    # Kellison
    return (-AnnuityImmediateA(n, i) + n) / i

def DecreasingAnnuityS(n, i):
    # Kellison
    return ((1 + i) ** n * n - AnnuityImmediateS(n, i)) / i

def v(i):
    # Kellison (1.10)
    return (1 / (1 + i))

def d(i):
    # Kellison 1.15a
    return i / (1 + i)

def delta(i):
    # Get the Force of Interest
    return math.log(1 + i)

def BondPriceBasic(C, F, r, i, n, m = 2):
    # Kellison 7.1 
    K = C * (1 + i / m) ** (-m * n)
    return F * r / m * AnnuityImmediateA(m * n, i / m) + K

def BondPricePD(C, F, r, i, n, m = 2):
    # Kellison 7.2
    return C + (F * r / m - C * i / m) * AnnuityImmediateA(m * n, i / m)

def BondPriceBaseAmount(C, F, r, i, n, m = 2):
    # Kellison 7.3
    g = (r / i) * F
    return g + (C - g) * v(i / m) ** (n * m)

def BondPriceMakeham(C, F, r, i, n, m = 2):
    # Kellison 7.4
    K = C * (1 + i / m) ** (-m * n)
    g = (F / C) * (r / m)
    return K + (g / i * m) * (C - K)

def DepreciationSF(A, S, n, t, j):
    # Kellison 8.22
    return ((A - S) / AnnuityImmediateS(n, j)) * (1 + j) ** (t - 1)

def DepreciationSL(A, S, n):
    # Kellison 8.23
    return (A - S) / n

def DepreciationDB(A, S, n, B):
    # Kellison 8.25, 8.27
    d = (1 - (S / A) ** (1 / n))
    return d * B

def DepreciationSOYD(A, S, n, t):
    # Kellison 8.29
    Sn = (n * (n + 1)) / 2  # Kellison 8.15
    return ((n - t + 1) / Sn) * (A - S)

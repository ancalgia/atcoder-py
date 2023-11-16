#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys
from decimal import Decimal

# import numpy


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


def getTriangleAreaByHelon(line1: Decimal, line2: Decimal, line3: Decimal) -> Decimal:
    s = (line1 + line2 + line3) / 2
    area = (s * (s - line1) * (s - line2) * (s - line3)).sqrt()
    return area


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# -52 -52
# -61 -76
# -2 -54
# 14 -11
#     """
# ).strip()  # "YES"


def main():
    (AX, AY), (BX, BY), (CX, CY), (DX, DY) = IALL(case)

    AX = Decimal(AX)
    AY = Decimal(AY)
    BX = Decimal(BX)
    BY = Decimal(BY)
    CX = Decimal(CX)
    CY = Decimal(CY)
    DX = Decimal(DX)
    DY = Decimal(DY)

    # AB = math.dist((AX, AY), (BX, BY))
    # BC = math.dist((BX, BY), (CX, CY))
    # CD = math.dist((CX, CY), (DX, DY))
    # DA = math.dist((DX, DY), (AX, AY))

    # AC = math.dist((AX, AY), (CX, CY))
    # BD = math.dist((BX, BY), (DX, DY))
    AB = ((AX - BX) ** 2 + (AY - BY) ** 2).sqrt()
    BC = ((BX - CX) ** 2 + (BY - CY) ** 2).sqrt()
    CD = ((CX - DX) ** 2 + (CY - DY) ** 2).sqrt()
    DA = ((DX - AX) ** 2 + (DY - AY) ** 2).sqrt()

    AC = ((CX - AX) ** 2 + (CY - AY) ** 2).sqrt()
    BD = ((BX - DX) ** 2 + (BY - DY) ** 2).sqrt()

    ABC = getTriangleAreaByHelon(AB, BC, AC)
    BCD = getTriangleAreaByHelon(BC, CD, BD)
    CDA = getTriangleAreaByHelon(CD, DA, AC)
    DAB = getTriangleAreaByHelon(DA, AB, BD)

    cond = abs((ABC + CDA) - (BCD + DAB)) < Decimal(0.0000000001)

    print("Yes") if cond else print("No")


if __name__ == "__main__":
    main()

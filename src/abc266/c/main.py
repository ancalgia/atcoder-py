#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys

# import numpy


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# def calcKakudo(pointA: tuple[int, int], pointB: tuple[int, int], pointC: tuple[int, int]):
#     # 点A,B,Cの座標（3次元座標上の場合）
#     np = numpy
#     a = np.array([pointA[0], pointA[1], 0])
#     b = np.array([pointB[0], pointB[1], 0])
#     c = np.array([pointC[0], pointC[1], 0])

#     # ベクトルを定義
#     vec_a = a - b
#     vec_c = c - b

#     # コサインの計算
#     length_vec_a = np.linalg.norm(vec_a)
#     length_vec_c = np.linalg.norm(vec_c)
#     inner_product = np.inner(vec_a, vec_c)
#     cos = inner_product / (length_vec_a * length_vec_c)

#     # 角度（ラジアン）の計算
#     rad = np.arccos(cos)

#     # 弧度法から度数法（rad ➔ 度）への変換
#     degree = np.rad2deg(rad)

#     return degree


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 0 0
# 1 0
# 1 1
# 0 1
#     """
# ).strip()
# case = dedent(
#     """
# 0 0
# 1 1
# -1 0
# 1 -1
#     """
# ).strip()


def main():
    (AX, AY), (BX, BY), (CX, CY), (DX, DY) = IALL(case)

    AC = (CX - AX, CY - AY)

    ACkatamuki = AC[0] / AC[1] if AC[1] != 0 else 0.0000000001

    ACseppen = AY - (ACkatamuki * AX)

    BSeppen = BY - (ACkatamuki * BX)
    DSeppen = DY - (ACkatamuki * DX)

    if (BSeppen < ACseppen < DSeppen) or (BSeppen > ACseppen > DSeppen):
        pass

    else:
        print("No")
        return

    BD = (DX - BX, DY - BY)

    BDkatamuki = BD[0] / BD[1] if BD[1] != 0 else 0.0000000001

    BDseppen = BY - (BDkatamuki * BX)

    CSeppen = CY - (BDkatamuki * CX)
    ASeppen = AY - (BDkatamuki * AX)

    if (CSeppen < BDseppen < ASeppen) or (CSeppen > BDseppen > ASeppen):
        pass

    else:
        print("No")
        return

    # kakudo1 = calcKakudo((AX, AY), (BX, BY), (CX, CY))
    # kakudo2 = calcKakudo((BX, BY), (CX, CY), (DX, DY))
    # kakudo3 = calcKakudo((CX, CY), (DX, DY), (AX, AY))
    # kakudo4 = calcKakudo((DX, DY), (AX, AY), (BX, BY))

    # print(kakudo1)
    # print(kakudo2)
    # print(kakudo3)
    # print(kakudo4)

    # if min(DX, BX) <= AX:
    #     print("No")
    #     return

    # if min(AY, CY) <= BY:
    #     print("No")
    #     return

    # if min(BX, DX) <= CX:
    #     print("No")
    #     return

    # if min(CY, AY) <= DY:
    #     print("No")
    #     return

    print("Yes")

    # if kakudo1 >= 180.0 or kakudo2 >= 180.0 or kakudo3 >= 180.0 or kakudo4 >= 180.0:
    #     print("No")

    # else:
    #     print("Yes")


if __name__ == "__main__":
    main()

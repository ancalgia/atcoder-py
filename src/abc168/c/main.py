#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "3 4 10 40"
# case = "3 4 10 40"


def main():
    A, B, H, M = IL(case)

    #  時針
    # 角度
    # jiKakudo = math.degrees((H / 6) * math.pi)
    hhKakudo = ((H + (M / 60)) / 6) * math.pi

    hhX = math.sin(hhKakudo) * A
    hhY = math.cos(hhKakudo) * A

    # 分針
    mmKakudo = (M / 30) * math.pi

    mmX = math.sin(mmKakudo) * B
    mmY = math.cos(mmKakudo) * B

    print(math.dist([hhX, hhY], [mmX, mmY]))


if __name__ == "__main__":
    main()

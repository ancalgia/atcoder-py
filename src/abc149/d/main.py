#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    NK, RSP, Ts = SL(case)

    N, K = IL(NK)
    R, S, P = IL(RSP)

    def getPojnt(hand: str):
        if hand == "r":
            return R
        elif hand == "s":
            return S
        else:
            return P

    revTs = Ts[::-1]

    result = 0

    hands: list[str] = []

    for t in revTs:
        if t == "r":
            tmpHand = "p"
        elif t == "s":
            tmpHand = "r"
        else:
            tmpHand = "s"

        if len(hands) >= K and hands[-K] == tmpHand:
            hands.append("*")
        else:
            hands.append(tmpHand)
            result += getPojnt(tmpHand)

    print(result)


if __name__ == "__main__":
    main()

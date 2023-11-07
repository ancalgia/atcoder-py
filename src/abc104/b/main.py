#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "AtCod"


def main():
    S, *_ = SL(case)

    if S[0] != "A":
        print("WA")
        return

    if not (S.count("A") == 1 and S.count("C") == 1):
        print("WA")
        return

    if S[2:-1].count("C") != 1:
        print("WA")
        return

    if S.replace("A", "").replace("C", "").lower() != S.replace("A", "").replace("C", ""):
        print("WA")
        return

    print("AC")


if __name__ == "__main__":
    main()

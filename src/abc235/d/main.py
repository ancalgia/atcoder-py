#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])
# case = "3 72"

result = 10**20

checkedSet: set[int] = set()


def chk(c: int, a: int, n: int, kaisu: int):
    global checkedSet

    if c in checkedSet:
        return

    checkedSet.add(c)

    if c == n:
        global result
        result = min(result, kaisu)
        return

    if len(str(c)) > len(str(n)):
        return

    kaisu += 1

    multic = c * a
    chk(multic, a, n, kaisu)

    if c > 10 and c % 10 != 0:
        shiftc = int(str(c)[-1] + str(c)[:-1])
        chk(shiftc, a, n, kaisu)


def main():
    A, N = IL(case)

    current = 1

    kaisu = 0

    chk(current, A, N, kaisu)

    global result

    if result == 10**20:
        print(-1)
    else:
        print(result)


if __name__ == "__main__":
    main()

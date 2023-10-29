#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 3
# 1 3 2
# 3 1 2
#     """
# ).strip()


def main():
    (N,), Ps, Qs = IALL(case)

    nums = [x for x in range(1, N + 1)]

    ptn = list(itertools.permutations(nums))
    ptn.sort()

    Ps = tuple(Ps)
    Qs = tuple(Qs)

    idx = 0
    for x in ptn:
        idx += 1
        if x == Ps:
            break

    idx2 = 0
    for x in ptn:
        idx2 += 1
        if x == Qs:
            break

    print(abs(idx - idx2))


if __name__ == "__main__":
    main()

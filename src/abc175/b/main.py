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
# 5
# 4 4 9 7 5
#     """
# ).strip()


def main():
    (N,), Ls = IALL(case)

    result = 0

    for x in range(0, N):
        t1 = Ls[x]

        for y in range(x + 1, N):
            t2 = Ls[y]

            for z in range(y + 1, N):
                t3 = Ls[z]
                tgts = sorted([t1, t2, t3])

                pass

                isUnique = tgts[0] != tgts[1] and tgts[0] != tgts[2] and tgts[1] != tgts[2]
                isMakeable = tgts[2] < tgts[0] + tgts[1]

                if isUnique and isMakeable:
                    result += 1
                else:
                    pass

    print(result)


if __name__ == "__main__":
    main()

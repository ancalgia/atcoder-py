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
# 2
# FLIP
# 6
# 1 1 3
# 2 0 0
# 1 1 2
# 1 2 3
# 2 0 0
# 1 1 4
#     """
# ).strip()


def main():
    N, S, Q, *Queries = SL(case)

    N = int(N)

    S1 = list(S[:N])
    S2 = list(S[N:])

    for x in Queries:
        T, A, B = map(int, x.split())

        if T == 1:
            tgt1 = S1 if A <= N else S2
            tgt2 = S1 if B <= N else S2

            (
                tgt1[(A - 1) % N],
                tgt2[(B - 1) % N],
            ) = (
                tgt2[(B - 1) % N],
                tgt1[(A - 1) % N],
            )

        else:
            S1, S2 = S2, S1

    print("".join(S1 + S2))
    pass


if __name__ == "__main__":
    main()

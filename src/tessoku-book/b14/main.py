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
# 6 30
# 5 1 18 9999 7 2 9
# """
# ).strip()


def main():
    (N, K), As = IALL(case)

    mae = As[: N // 2]

    half1Set = set(itertools.chain.from_iterable([itertools.combinations(mae, x) for x in range(len(mae) + 1)]))

    half1sums = set([sum(x) for x in half1Set])

    usiro = As[N // 2 :]

    half2Set = set(itertools.chain.from_iterable([itertools.combinations(usiro, x) for x in range(len(usiro) + 1)]))

    half2sums = set([sum(x) for x in half2Set])

    for x in half1sums:
        if (K - x) in half2sums:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()

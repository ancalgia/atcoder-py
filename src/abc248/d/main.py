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
# 3 1 4 1 5
# 4
# 1 5 1
# 2 4 3
# 1 5 2
# 1 3 3
#     """
# ).strip()


def main():
    (N,), As, (Q,), *Queries = IALL(case)

    piyo: dict[int, list[int]] = {}

    for idx, x in enumerate(As, 1):
        if x in piyo:
            piyo[x].append(idx)
        else:
            piyo[x] = [idx]

    for query in Queries:
        if query[2] not in piyo:
            print(0)
            continue

        allTgt = bisect.bisect_left(piyo[query[2]], query[1] + 1)
        minusTgt = bisect.bisect_left(piyo[query[2]], query[0])

        print(allTgt - minusTgt)


if __name__ == "__main__":
    main()

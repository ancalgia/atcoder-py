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
# alice 31
# bob 41
# carol 5
# dave 92
# ellen 65
#     """
# ).strip()


def main():
    N, *SAs = SL(case)

    SAs = [x.split() for x in SAs]

    youngest = min([int(x[1]) for x in SAs])

    youngIdx = [idx for idx, x in enumerate(SAs) if int(x[1]) == youngest][0]

    withStart = SAs[youngIdx:] + SAs[:youngIdx]

    for x in withStart:
        print(x[0])

    pass


if __name__ == "__main__":
    main()

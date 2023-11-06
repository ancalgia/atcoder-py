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
# ..........
# ..........
# ..........
# ..........
# ...######.
# ...######.
# ...######.
# ...######.
# ..........
# ..........
#     """
# ).strip()


def main():
    matrix = SL(case)

    minH = 9999999
    maxH = -9999999

    minW = 9999999
    maxW = -9999999

    for idx, x in enumerate(matrix):
        if "#" in x:
            minH = min([minH, idx + 1])
            maxH = max([maxH, idx + 1])

    for idx, x in enumerate(zip(*matrix)):
        pass
        parsedx = "".join(x)

        if "#" in parsedx:
            minW = min([minW, idx + 1])
            maxW = max([maxW, idx + 1])

    pass

    print(f"{minH} {maxH}")
    print(f"{minW} {maxW}")


if __name__ == "__main__":
    main()

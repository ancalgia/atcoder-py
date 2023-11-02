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
# 19 18
# ###......###......
# ###......###......
# ###..#...###..#...
# ..............#...
# ..................
# ..................
# ......###......###
# ......###......###
# ......###......###
# .###..............
# .###......##......
# .###..............
# ............###...
# ...##.......###...
# ...##.......###...
# .......###........
# .......###........
# .......###........
# ........#.........
#     """
# ).strip()


def main():
    NM, *matrix = SL(case)

    N, M = IL(NM)

    resultSet: set[tuple[int, int]] = set()

    for x in range(N - 8):
        for y in range(M - 8):
            tgt = [z[y : y + 9] for z in matrix[x : x + 9]]

            if all(
                [
                    tgt[0][:4] == "###.",
                    tgt[1][:4] == "###.",
                    tgt[2][:4] == "###.",
                    tgt[3][:4] == "....",
                    tgt[5][5:] == "....",
                    tgt[6][5:] == ".###",
                    tgt[7][5:] == ".###",
                    tgt[8][5:] == ".###",
                ]
            ):
                resultSet.add((x + 1, y + 1))

    for x in sorted(list(resultSet)):
        print(*x)


if __name__ == "__main__":
    main()

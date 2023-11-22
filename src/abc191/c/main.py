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
# 10 10
# ..........
# ..#.#.#.#.
# .########.
# ..#.#.#.#.
# ........#.
# ..#.#.#.#.
# .########.
# ..#.#.#.#.
# .##.....#.
# ..........
#     """
# ).strip()

# case = dedent(
#     """
# 3 3
# ...
# .#.
# ...
#     """
# ).strip()


def main():
    HW, *matrix = SL(case)

    # 図を拡大する
    matrix = itertools.chain.from_iterable([[x, x, x] for x in matrix])

    matrix = ["".join([z * 3 for z in x]) for x in matrix]

    H, W = IL(HW)

    result = 0

    for x in range(H * 3):
        for y in range(W * 3):
            if matrix[x][y] == "#":
                tmp = [
                    matrix[x][y + 1] == ".",
                    matrix[x + 1][y + 1] == ".",
                    matrix[x + 1][y] == ".",
                    matrix[x + 1][y - 1] == ".",
                    matrix[x][y - 1] == ".",
                    matrix[x - 1][y - 1] == ".",
                    matrix[x - 1][y] == ".",
                    matrix[x - 1][y + 1] == ".",
                ].count(True)

                if tmp != 3 and tmp != 0 and tmp != 2:
                    result += 1

    print(result)


if __name__ == "__main__":
    main()

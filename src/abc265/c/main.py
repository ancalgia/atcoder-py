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
# 9 44
# RRDDDDRRRDDDRRRRRRDDDRDDDDRDDRDDDDDDRRDRRRRR
# RRRDLRDRDLLLLRDRRLLLDDRDLLLRDDDLLLDRRLLLLLDD
# DRDLRLDRDLRDRLDRLRDDLDDLRDRLDRLDDRLRRLRRRDRR
# DDLRRDLDDLDDRLDDLDRDDRDDDDRLRRLRDDRRRLDRDRDD
# RDLRRDLRDLLLLRRDLRDRRDRRRDLRDDLLLLDDDLLLLRDR
# RDLLLLLRDLRDRLDDLDDRDRRDRLDRRRLDDDLDDDRDDLDR
# RDLRRDLDDLRDRLRDLDDDLDDRLDRDRDLDRDLDDLRRDLRR
# RDLDRRLDRLLLLDRDRLLLRDDLLLLLRDRLLLRRRRLLLDDR
# RRRRDRDDRRRDDRDDDRRRDRDRDRDRRRRRRDDDRDDDDRRR
#     """
# ).strip()
# # 2_3
# # RRD
# # ULL


def main():
    HW, *rest = SL(case)

    H, W = map(int, HW.split())

    matrix = [list(x) for x in rest]

    current = [0, 0]
    while True:
        yuka = matrix[current[0]][current[1]]

        if yuka == "U":
            next = [current[0] - 1, current[1]]
        elif yuka == "D":
            next = [current[0] + 1, current[1]]
        elif yuka == "L":
            next = [current[0], current[1] - 1]
        elif yuka == "R":
            next = [current[0], current[1] + 1]
        else:
            print(-1)
            return

        matrix[current[0]][current[1]] = "X"

        if any([next[0] < 0, H <= next[0], next[1] < 0, W <= next[1]]):
            print(f"{current[0]+1} {current[1]+1}")
            return

        current = next


if __name__ == "__main__":
    main()

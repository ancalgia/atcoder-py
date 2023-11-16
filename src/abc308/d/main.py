#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys

sys.setrecursionlimit(10**6)

# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


def createWall(matrix: list[list[str]], H: int, W: int, wall: str) -> list[list[str]]:
    return [[wall] * (W + 2)] + [[wall] + x + [wall] for x in matrix] + [[wall] * (W + 2)]


nextDict = {"s": "n", "n": "u", "u": "k", "k": "e", "e": "s"}


def walk(
    curr: tuple[int, int],
    walled: list[list[str]],
    trace: set[tuple[int, int]],
    char: str,
    goal: tuple[int, int],
):
    cp = trace

    if curr in cp:
        return
    cp.add(curr)

    if curr == goal:
        print("Yes")
        exit()

    if walled[curr[0] + 1][curr[1]] == nextDict[char]:
        walk((curr[0] + 1, curr[1]), walled, cp, nextDict[char], goal)
    if walled[curr[0]][curr[1] + 1] == nextDict[char]:
        walk((curr[0], curr[1] + 1), walled, cp, nextDict[char], goal)
    if walled[curr[0] - 1][curr[1]] == nextDict[char]:
        walk((curr[0] - 1, curr[1]), walled, cp, nextDict[char], goal)
    if walled[curr[0]][curr[1] - 1] == nextDict[char]:
        walk((curr[0], curr[1] - 1), walled, cp, nextDict[char], goal)

    return


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 2 3
# sns
# euk
#     """
# ).strip()


def main():
    HW, *matrix = SL(case)

    H, W = IL(HW)

    matrix = list(map(list, matrix))

    walled = createWall(matrix, H, W, "*")

    current: tuple[int, int] = (1, 1)
    goal: tuple[int, int] = (H, W)

    trace: set[tuple[int, int]] = set()

    if walled[1][1] != "s":
        # 足元がsじゃなきゃ即死
        print("No")
        return

    walk(current, walled, trace, "s", goal)

    print("No")


if __name__ == "__main__":
    main()

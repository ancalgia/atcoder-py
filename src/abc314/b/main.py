#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    (N,), *rest = IALL(case)

    playerDict: dict[int, list[int]] = dict()

    for x in range(N):
        tgt = x * 2

        playerDict[x + 1] = rest[tgt + 1]

    ball = rest[-1][0]

    winners: dict[int, list[int]] = dict()

    for x in playerDict:
        if ball in playerDict[x]:
            winners[x] = playerDict[x]

    small = 99999999999999999

    for x in winners:
        cnt = len(winners[x])

        small = min([small, cnt])

    result: list[int] = []

    for x in winners:
        if len(winners[x]) == small:
            result.append(x)

    if len(result) == 0:
        print(0)
        print("")
        return
    else:
        print(len(result))
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

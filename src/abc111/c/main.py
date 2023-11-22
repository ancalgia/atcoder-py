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
    (N,), Vs = IALL(case)

    odds = [x for idx, x in enumerate(Vs, 1) if idx % 2 == 1]
    evens = [x for idx, x in enumerate(Vs, 1) if idx % 2 == 0]

    oddCounter = collections.Counter(odds).most_common()
    evenCounter = collections.Counter(evens).most_common()

    minMoves = 10**10

    # 奇数を軸とする場合
    oddMove = (N // 2) - oddCounter[0][1]

    if oddCounter[0] != evenCounter[0]:
        evenMove = (N // 2) - evenCounter[0][1]
    else:
        if len(evenCounter) != 1:
            evenMove = (N // 2) - evenCounter[1][1]
        else:
            evenMove = N // 2

    minMoves = min(minMoves, oddMove + evenMove)

    # 偶数を軸とする場合
    evenMove = (N // 2) - evenCounter[0][1]

    if evenCounter[0] != oddCounter[0]:
        oddMove = (N // 2) - oddCounter[0][1]
    else:
        if len(oddCounter) != 1:
            oddMove = (N // 2) - oddCounter[1][1]
        else:
            oddMove = N // 2

    minMoves = min(minMoves, oddMove + evenMove)

    print(minMoves)


if __name__ == "__main__":
    main()

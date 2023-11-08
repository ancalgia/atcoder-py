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
    (N, M), *SCs = IALL(case)

    maybeResult: list[str] = ["0" for x in range(N)]

    for s, c in SCs:
        if s == 1 and c == 0:
            if N == 1:
                print(0)
                return
            else:
                print(-1)
                return

        if maybeResult[s - 1] != "0" and maybeResult[s - 1] != str(c):
            print(-1)
            return

        maybeResult[s - 1] = str(c)

    if maybeResult[0] == "0" and N != 1:
        maybeResult[0] = "1"

    result = int("".join(maybeResult))

    if len(str(result)) != N:
        print(-1)
    else:
        print(result)


if __name__ == "__main__":
    main()

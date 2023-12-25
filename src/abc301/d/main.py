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
    S, N = SL(case)

    N = int(N)

    hatenaCount = S.count("?")

    # allPtn = list(itertools.product(*[["1", "0"] for x in range(hatenaCount)]))

    allZero = int(S.replace("?", "0"), 2)

    allOne = int(S.replace("?", "1"), 2)

    if N < allZero:
        print(-1)
        return

    if N >= allOne:
        print(allOne)
        return

    results: list[str] = []

    listedS = list(S)

    for x in range(hatenaCount):
        tmp = S
        for r in results:
            tmp = tmp.replace("?", r, 1)

        tmp = tmp.replace("?", "1", 1).replace("?", "0")

        tmpNum = int(tmp, 2)

        if tmpNum < N:
            results.append("1")
        elif tmpNum > N:
            results.append("0")
        elif tmpNum == N:
            print(tmpNum)
            return

    lastResult = S
    for r in results:
        lastResult = lastResult.replace("?", r, 1)

    print(int(lastResult, 2))


if __name__ == "__main__":
    main()

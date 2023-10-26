#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "aab 2"


def main():
    S, K = case.split()

    K = int(K)

    allPtn = list(set(itertools.permutations(S)))

    allPtn = ["".join(x) for x in allPtn]

    allPtn = sorted(allPtn)

    # result = allPtn[K - 1]
    print(allPtn[K - 1])

    pass


if __name__ == "__main__":
    main()

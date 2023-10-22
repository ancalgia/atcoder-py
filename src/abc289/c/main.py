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
    (N, M), *rest = IALL(case)

    As = [x for idx, x in enumerate(rest) if idx % 2 == 1]

    allSet = [list(itertools.combinations(As, x)) for x in range(1, M + 1)]

    flat1Set = itertools.chain.from_iterable(allSet)

    flat2Set = [list(set(itertools.chain.from_iterable(x))) for x in flat1Set]

    lenSet = [len(x) for x in flat2Set]

    print(lenSet.count(N))


if __name__ == "__main__":
    main()

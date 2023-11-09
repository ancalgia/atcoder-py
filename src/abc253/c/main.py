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
    (N,), *Queries = IALL(case)

    counter: collections.Counter[int] = collections.Counter()

    currentMin = 999999999999999999
    currentMax = 0

    for q in Queries:
        if q[0] == 1:
            counter[q[1]] += 1
            currentMin = min([currentMin, q[1]])
            currentMax = max([currentMax, q[1]])

        elif q[0] == 2:
            counter[q[1]] -= min([q[2], counter[q[1]]])

            if counter[q[1]] == 0:
                counter.pop(q[1])
                if currentMin == q[1]:
                    currentMin = min(counter) if len(counter) > 0 else 999999999999999999
                if currentMax == q[1]:
                    currentMax = max(counter) if len(counter) > 0 else 0

        else:
            print(currentMax - currentMin)


if __name__ == "__main__":
    main()

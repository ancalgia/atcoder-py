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
    (N, M), As, *BCs = IALL(case)

    hpAs: list[int] = As

    heapq.heapify(hpAs)

    BCs.sort(key=lambda x: x[1], reverse=True)

    for b, c in BCs:
        for x in range(b):
            popped = heapq.heappop(hpAs)

            if popped < c:
                heapq.heappush(hpAs, c)
            else:
                heapq.heappush(hpAs, popped)
                break

    print(sum(hpAs))


if __name__ == "__main__":
    main()

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
    (N,), As = IALL(case)

    maxA = max(As)

    aveA = math.floor(sum(As) / len(As))

    lows = [x for x in As if x < aveA]
    highs = [x for x in As if x > aveA + 1]

    lowNeeds = sum([abs(aveA - x) for x in lows])
    highNeeds = sum([abs((aveA + 1) - x) for x in highs])

    print(max(lowNeeds, highNeeds))

    # result = 0

    # hp = As

    # heapq.heapify(hp)

    # while True:
    #     p1 = heapq.heappop(hp)

    #     if abs(maxA - p1) <= 1:
    #         print(result)
    #         return

    #     heapq.heappush(hp, p1 + 1)

    #     p2 = heapq.heappop(hp)

    #     result += 1

    #     if abs(maxA - p2) <= 1:
    #         print(result)
    #         return

    #     heapq.heappush(hp, p2 + 1)

    pass


if __name__ == "__main__":
    main()

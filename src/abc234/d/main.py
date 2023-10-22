#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 3 2
# 1 2 3
#     """
# ).strip()


def main():
    (N, K), Ps = IALL(case)

    # currentmin = min([Ps[:K]])

    # currChecker: collections.deque[int] | None = None
    currChecker: list[int] = sorted(Ps[0:K])
    heapq.heapify(currChecker)
    print(currChecker[0])

    for x in range(K + 1, N + 1):
        # if len(currChecker) == 0:
        # if len(currChecker) == 0:
        #     # currChecker = Ps[0:K]
        #     # currChecker = collections.deque(sorted(Ps[0:K]))
        #     # heapq. currChecker

        #     # currChecker.sort(reverse=True)
        #     # currChecker.sort()

        #     print(currChecker[0])

        # else:
        if currChecker[0] < Ps[x - 1]:
            # currChecker.append(Ps[x - 1])

            # bisect.insort_left(currChecker, Ps[x - 1])
            heapq.heappush(currChecker, Ps[x - 1])
            heapq.heappop(currChecker)

        # currChecker.sort(reverse=True)

        print(currChecker[0])

        # currChecker.pop()
    pass


if __name__ == "__main__":
    main()

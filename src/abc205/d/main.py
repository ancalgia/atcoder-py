#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# case: str = "".join([x for x in sys.stdin])


from textwrap import dedent

case = dedent(
    """
4 3
3 5 6 7
2
5
3
    """
).strip()


def main():
    (N, Q), As, *Queries = IALL(case)

    Queries = [x[0] for x in Queries]

    tmp = 0

    lastNum = 0

    excludeCountList: list[dict[int, int]] = []

    for a in As:
        tmp += a - 1 - lastNum

        excludeCountList.append({a: tmp})

        lastNum = a

    print(excludeCountList)

    # 2 → 2
    # 5 → 9
    # 3 → 4

    for q in Queries:
        hoge = bisect.bisect_left(As, q)
        print(bisect.bisect_left(As, q) + q)

    pass


if __name__ == "__main__":
    main()

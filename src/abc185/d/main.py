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
# 920234074 10
# 124539164 421951379 224621736 172538952 447200274 257167083 325128564 6332923 697456728 394383238
#     """
# ).strip()


def main():
    (N, M), *As = IALL(case)

    if M == 0 and N != 0:
        print(1)
        return

    As = As[0]

    if N == M:
        print(0)
        return

    sortedAs = sorted(As)

    withStartAndEnd = [0] + sortedAs + [N + 1]

    diffs = [r - l - 1 for l, r in zip(withStartAndEnd, withStartAndEnd[1:])]

    stamp = min([x for x in diffs if x != 0])

    result = 0

    for x in diffs:
        if x == 0:
            continue

        d, m = divmod(x, stamp)

        result += d + (1 if m else 0)

    print(result)


if __name__ == "__main__":
    main()

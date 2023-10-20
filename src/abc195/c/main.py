#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "1000000"
# case = "999999"
# case = "1010"
# case = "10000"


def main():
    N = int(case)

    if N < 1000:
        print(0)
        return

    d, m = divmod(len(str(N)), 3)

    result = 0

    for x in range(d):
        result += x * 999 * (1000**x)
        pass

    # result += (d) * (N - (10 ** (len(str(N)) - 1)) + 1)
    result += (d) * (N - (10 ** (d * 3)) + 1)

    print(result)

    pass


if __name__ == "__main__":
    main()

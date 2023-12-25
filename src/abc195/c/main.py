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
# case = "193162"  # 192163
# case = "27182818284590"  # 107730272137364


def main():
    N = int(case)

    if N < 1000:
        print(0)
        return

    ketasu = len(str(N))

    commas = (ketasu - 1) // 3

    result = 0

    tmp999 = ""

    for x in range(commas):
        tmp999 += "999"

        result += N - int(tmp999)  # * comma

    print(result)


if __name__ == "__main__":
    main()

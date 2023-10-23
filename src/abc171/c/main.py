#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys

import numpy


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# case: str = "".join([x for x in sys.stdin])

case = "703"


def main():
    N = int(case)

    caesar = str.maketrans(
        "123456789ABCDEFGHIJKLMNOP0",
        "abcdefghijklmnopqrstuvwxyz",
    )

    # t = numpy.base_repr(N, 26)

    # print(t.translate(caesar))
    result = []

    result.append((N) % 26)
    currN = N

    for x in range(1, 500):
        if N > 26**x:
            result.append((N - 26**x) // (26**x))

        else:
            break

    # while True:
    #     d, m = divmod(currN, 26)

    #     # result.append(m)

    #     result.append(m)

    #     if d != 0:
    #         currN = d

    #         if d <= 26 and m == 0:
    #             result.append(d - 1)

    #             break
    #     else:
    #         break

    #     pass

    resultStr = ""

    for x in reversed(result):
        hoge = numpy.base_repr(x, 26)
        resultStr += hoge.translate(caesar)

    print(resultStr)
    pass


if __name__ == "__main__":
    main()

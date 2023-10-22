#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "10 3 5"
# case = "1000000000 314 159"

# case = "433933447 476190629 262703497"  #

# case = "211047202 971407775 628894325"  # 22270460841538003
# case = "1000000000 430302156 430302156"  # 499999999209093532
# case = "901169605 49 91"  # 393941847880945560
# print(393395465900209787 - 393941847880945560)


def main():
    N, A, B = IL(case)

    # AB = A * B
    AB = math.lcm(A, B)

    # sumN = int((1 + N) * (N / 2))
    # sumA = round((A + (N - (N % A))) * ((N // A) / 2))
    # sumB = round((B + (N - (N % B))) * ((N // B) / 2))

    # sumAB = round((AB + (N - (N % AB))) * ((N // AB) / 2))
    sumN = ((1 + N) * (N)) // 2

    sumA = ((A + (N - (N % A))) * ((N // A))) // 2
    if A == B:
        print(sumN - sumA)
        return
    sumB = ((B + (N - (N % B))) * ((N // B))) // 2

    sumAB = ((AB + (N - (N % AB))) * ((N // AB))) // 2

    print(sumN - (sumA + sumB) + sumAB)

    pass


if __name__ == "__main__":
    main()

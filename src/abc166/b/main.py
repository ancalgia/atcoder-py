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
    (N, K), *rest = IALL(case)

    okasi_holders = [x for idx, x in enumerate(rest) if idx % 2 == 1]

    flat_okasi_holders = set(itertools.chain.from_iterable(okasi_holders))

    print(N - len(flat_okasi_holders))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "101"
# case = "999983"


def main():
    N = int(case)

    if N % 2 == 0:
        print(-1)
        return

    tmp = N

    cnt = 1

    while True:
        tmp += N

        hoge = str(tmp)

        if len(set(hoge)) == 1 and hoge[0] == "7":
            print(len(hoge))
            return

        cnt += 1

    #     if len(str(tmp)) >= 4:
    #         d, m = divmod(tmp, 10)

    #         tmp = d - m * 2

    #     if tmp % N == 0:
    #         print(x)
    #         return
    #     continue

    # print(-1)


if __name__ == "__main__":
    main()

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
    (N,), Ps = [list(map(int, x.split())) for x in case.splitlines()]

    reversedPs = list(reversed(Ps))

    tgtidx = 99999
    current_num = 0
    for idx, x in enumerate(reversedPs):
        if idx == 0:
            current_num = x
            continue

        else:
            if current_num < x:
                tgtidx = idx
                break
            else:
                current_num = x
                continue

    changenum1st = max([x for x in reversedPs[:tgtidx] if x < reversedPs[tgtidx]])
    changeidx1st = reversedPs.index(changenum1st)

    (reversedPs[tgtidx], reversedPs[changeidx1st]) = (reversedPs[changeidx1st], reversedPs[tgtidx])

    restSorted = sorted(reversedPs[:tgtidx])

    result = restSorted + reversedPs[tgtidx:]

    result.reverse()

    print(*result)


if __name__ == "__main__":
    main()

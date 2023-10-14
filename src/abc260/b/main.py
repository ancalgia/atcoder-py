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
    (N, X, Y, Z), As, Bs = IALL(case)

    students: list[list[int]] = []

    passedList = []

    for idx, (a, b) in enumerate(zip(As, Bs)):
        students.append([a, b, a + b, idx])

    # sortBySugaku = numpy.lexsort(students, axis=[0, 3]).tolist()[::-1]

    sortBySugaku = sorted(students, key=lambda x: (x[0], -x[3]), reverse=True)

    passedList.extend(sortBySugaku[:X])

    sortBySugaku = sortBySugaku[X:]

    # sortByEng = numpy.sort(sortBySugaku, axis=1).tolist()[::-1]

    sortByEng = sorted(sortBySugaku, key=lambda x: (x[1], -x[3]), reverse=True)

    passedList.extend(sortByEng[:Y])

    sortByEng = sortByEng[Y:]

    # sortBySum = numpy.sort(sortByEng, axis=2).tolist()[::-1]

    sortBysum = sorted(sortByEng, key=lambda x: (x[2], -x[3]), reverse=True)

    passedList.extend(sortBysum[:Z])

    passedList = sorted(passedList, key=lambda x: x[3])

    for x in passedList:
        print(x[3] + 1)

    pass


if __name__ == "__main__":
    main()

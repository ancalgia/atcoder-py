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
    N, *S = case.splitlines()

    persons = [list(map(int, x.split())) for x in S[:-1]]

    personsWithDirectionSet = set([(x[0], x[1], d) for x, d in zip(persons, S[-1])])

    personAxisYList = [x[1] for x in personsWithDirectionSet]

    AxisYCounter = collections.Counter(personAxisYList).most_common()

    mustCheckAxisY = set([x[0] for x in AxisYCounter if x[1] >= 2])

    pass

    for y in mustCheckAxisY:
        tgt = set(filter(lambda x: x[1] == y, personsWithDirectionSet))

        rights = set(filter(lambda x: x[2] == "R", tgt))
        lefts = set(filter(lambda x: x[2] == "L", tgt))

        if len(rights) == 0 or len(lefts) == 0:
            continue

        minRight = min(filter(lambda x: x[2] == "R", tgt))
        maxLeft = max(filter(lambda x: x[2] == "L", tgt))

        if minRight <= maxLeft:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()

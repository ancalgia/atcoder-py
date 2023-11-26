#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int):
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = collections.defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 6
# 1 3
# 1 5
# 1 12
# 3 5
# 3 12
# 5 12
#     """
# ).strip()


def main():
    (N,), *ABs = IALL(case)

    allNums = sorted(set(itertools.chain.from_iterable(ABs + [[1]])))

    allNumDict: dict[int, int] = dict()
    allNumDictRev: dict[int, int] = dict()

    for idx, x in enumerate(allNums, 1):
        allNumDict[idx] = x
        allNumDictRev[x] = idx

    # maxFloor = max(map(max, ABs))
    uf = UnionFind(len(allNums))

    graph = [[] for _ in range(len(allNums))]

    for a, b in ABs:
        # a -= 1
        # b -= 1
        a = allNumDictRev[a] - 1
        b = allNumDictRev[b] - 1

        graph[a].append(b)
        graph[b].append(a)
        uf.union(a, b)

    with1 = uf.members(0)

    print(allNumDict[max(with1) + 1])
    return

    # upDict: dict[int, set[int]] = dict()
    # downDict: dict[int, set[int]] = dict()

    # for ab in ABs:
    #     ab.sort()

    #     if ab[0] not in upDict:
    #         upDict[ab[0]] = {ab[1]}
    #     else:
    #         upDict[ab[0]].add(ab[1])

    #     if ab[1] not in downDict:
    #         downDict[ab[1]] = {ab[0]}
    #     else:
    #         downDict[ab[1]].add(ab[0])

    # currentAble = {1}

    # while True:
    #     tmpLen = len(currentAble)

    #     newAble: set[int] = set()
    #     for x in currentAble:
    #         if x in upDict:
    #             newAble.update(upDict[x])
    #             upDict.pop(x)
    #         if x in downDict:
    #             newAble.update(downDict[x])
    #             downDict.pop(x)

    #     currentAble.update(newAble)

    #     if len(currentAble) == tmpLen:
    #         print(max(currentAble))
    #         return

    # pass


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


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


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 7 7
# 1 3
# 2 7
# 3 4
# 4 5
# 4 6
# 5 6
# 6 7
#     """
# ).strip()


def main():
    (N, M), *ABs = IALL(case)

    uf = UnionFind(N)

    graph = [[] for _ in range(N)]

    for a, b in ABs:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
        uf.union(a, b)

    allcount = uf.group_count()

    result = 0

    for ignore in range(M):
        uf = UnionFind(N)

        graph = [[] for _ in range(N)]

        for idx, (a, b) in enumerate(ABs):
            if idx == ignore:
                continue
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)
            uf.union(a, b)

        if uf.group_count() != allcount:
            result += 1

    print(result)

    pass


if __name__ == "__main__":
    main()

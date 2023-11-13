#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys
from collections import defaultdict


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
        group_members = defaultdict(list)
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
# 4 3
# 1 3
# 4 2
# 3 2
#     """
# ).strip()


def main():
    (N, M), *UVs = IALL(case)

    if N != M + 1:
        print("No")
        return

    # counter = collections.Counter(itertools.chain.from_iterable([list(x) for x in UVs])).most_common()

    # if counter[0][1] != 2:
    #     print("No")
    #     return

    # if counter[-1][1] != 1:
    #     print("No")
    #     return

    # if counter[-1][1] != counter[-2][1]:
    #     print("No")
    #     return

    # ここから本番
    # start = counter[-1][0]

    uf = UnionFind(N)

    one_num = 0  # 次数1のカウント
    two_num = 0  # 次数2のカウント

    graph = [[] for _ in range(N)]

    pass

    for u, v in UVs:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        uf.union(u, v)

    for one in graph:
        if len(one) == 1:
            one_num += 1
        elif len(one) == 2:
            two_num += 1
        else:
            print("No")
            exit()

    if one_num == 2 and uf.group_count() == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

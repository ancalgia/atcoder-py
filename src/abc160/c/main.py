#!/usr/bin/env python3


def main():
    K, N = list(map(int, input().split()))

    As = list(map(int, input().split()))

    As.append(As[0] + K)

    diffs = [r - l for l, r in zip(As, As[1:])]

    maxDiff = max(diffs)

    print(K - maxDiff)

    pass


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys

case: str = "".join([x for x in sys.stdin])


def main():
    X = int(case)

    gohyaku = X // 500

    go = (X % 500) // 5

    print(gohyaku * 1000 + go * 5)


if __name__ == "__main__":
    main()

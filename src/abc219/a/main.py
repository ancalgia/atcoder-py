#!/usr/bin/env python3

import sys

case: str = "".join([x for x in sys.stdin])


def main():
    X = int(case)

    if X >= 90:
        print("expert")
        return

    elif X >= 70:
        print(90 - X)
    elif X >= 40:
        print(70 - X)
    else:
        print(40 - X)


if __name__ == "__main__":
    main()

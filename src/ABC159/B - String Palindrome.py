import itertools
import math
from typing import Literal


def main(case: str) -> None:
    S, *_ = case.splitlines()

    lenS = len(S)

    if lenS == 1:
        print("No")
        return

    if S != S[::-1]:
        print("No")
        return

    top = S[: int((lenS - 1) / 2)]
    end = S[int((lenS + 3) / 2) - 1 :]

    if lenS == 3:
        print("Yes")
        return

    # if top != top[::-1] or end != end[::-1]:
    if top != end:
        print("No")
        return

    print("Yes")


if __file__.endswith("Main.py"):
    import sys

    case: str = "".join([x for x in sys.stdin])
    main(case)
    exit()


else:
    print("テスト")
    from textwrap import dedent

    test_list: list[str] = [
        """
akasaka
        """,
        """
level
        """,
        """
atcoder
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

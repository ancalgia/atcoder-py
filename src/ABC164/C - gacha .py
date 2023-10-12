import itertools
import math
from typing import Literal


def main(case: str) -> None:
    N, *rest = case.splitlines()

    hoge = set(rest)

    print(len(hoge))


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
3
apple
orange
apple
        """,
        """
5
grape
grape
grape
grape
grape
        """,
        """
4
aaaa
a
aaa
aa
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

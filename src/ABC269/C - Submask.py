import itertools
from typing import Literal


def convert(x: str) -> list[str]:
    pass
    if x == "0":
        return ["0"]
    else:
        return ["1", "0"]


def main(case: str) -> None:
    N = int(case)

    bitN = bin(N)[2:]

    bitlist = [convert(x) for x in bitN]

    all_patterns = itertools.product(*bitlist)

    all_pattens_10digit = [int("".join(x), 2) for x in all_patterns]

    all_pattens_10digit.sort()

    [print(x) for x in all_pattens_10digit]


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
11
        """,
        """
0
        """,
        """
576461302059761664
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

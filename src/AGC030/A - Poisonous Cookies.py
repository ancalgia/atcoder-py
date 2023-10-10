import itertools
import math


def main(case: str) -> None:
    A, B, C = list(map(int, case.split()))

    eatable_poison_count = min([A + B + 1, C])

    print(B + eatable_poison_count)


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
3 1 4
        """,
        """
5 2 9
        """,
        """
8 8 1
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

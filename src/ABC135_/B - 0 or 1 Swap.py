import itertools
import math


def main(case: str) -> None:
    (N,), Ps = [list(map(int, x.split())) for x in case.splitlines()]

    ng_count = 0

    for idx, x in enumerate(Ps, 1):
        if idx != x:
            ng_count += 1

    print("YES" if ng_count == 0 or ng_count == 2 else "NO")


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
5
5 2 3 4 1
        """,
        """
5
2 4 3 5 1
        """,
        """
7
1 2 3 4 5 6 7
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

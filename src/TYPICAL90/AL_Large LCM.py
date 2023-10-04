import bisect
import itertools
import math


def main(case: str) -> None:
    N, M = list(map(int, case.split()))

    lcm = math.lcm(N, M)

    print(lcm if lcm <= 10**18 else "Large")


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
4 6
        """,
        """
1000000000000000000 3
        """,
        """
1000000000000000000 1
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

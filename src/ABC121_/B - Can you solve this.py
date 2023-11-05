import itertools
import math
from typing import Literal


def main(case: str) -> None:
    (N, M, C), Bs, *As = [list(map(int, x.split())) for x in case.splitlines()]

    count = 0

    for a in As:
        ans = sum([x * b for x, b in zip(a, Bs)]) + C

        count += 1 if ans > 0 else 0

    print(count)


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
2 3 -10
1 2 3
3 2 1
1 2 2
        """,
        """
5 2 -4
-2 5
100 41
100 40
-3 0
-6 -2
18 -13
        """,
        """
3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

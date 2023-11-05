import itertools
import math
from typing import Literal


def main(case: str) -> None:
    A, B = list(map(int, case.split()))

    alllength = math.sqrt(A**2 + B**2)

    gyaku = 1 / alllength

    print(str(A * gyaku) + " " + str(B * gyaku))


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
3 4
        """,
        """
1 0
        """,
        """
246 402
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

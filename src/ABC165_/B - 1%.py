import itertools
import math


def main(case: str) -> None:
    N = int(case)

    elapsed_years = 0

    depo = 100

    if depo >= N:
        print(0)
        return

    while 1:
        elapsed_years += 1
        # depo = math.floor(depo * 1.01)
        depo += depo // 100

        if depo >= N:
            break

    print(elapsed_years)


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
103
        """,
        """
1000000000000000000
        """,
        """
1333333333
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

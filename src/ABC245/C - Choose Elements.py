import itertools
from typing import Literal


def main(case: str) -> None:
    (N, K), As, Bs = [list(map(int, x.split())) for x in case.splitlines()]

    # 次で使っていい値（0＝両方）
    enable_next_start = [True, True]

    for x in range(N - 1):
        if enable_next_start == [True, True]:
            result = [
                abs(As[x] - As[x + 1]) <= K or abs(Bs[x] - As[x + 1]) <= K,
                abs(As[x] - Bs[x + 1]) <= K or abs(Bs[x] - Bs[x + 1]) <= K,
            ]
        elif enable_next_start == [True, False]:
            result = [
                abs(As[x] - As[x + 1]) <= K,
                abs(As[x] - Bs[x + 1]) <= K,
            ]
        else:
            pass
            result = [
                abs(Bs[x] - As[x + 1]) <= K,
                abs(Bs[x] - Bs[x + 1]) <= K,
            ]

        if any(result):
            enable_next_start = result
        else:
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
5 4
9 8 3 7 2
1 6 2 9 5
        """,
        """
4 90
1 1 1 100
1 2 3 100
        """,
        """
4 1000000000
1 1 1000000000 1000000000
1 1000000000 1 1000000000
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

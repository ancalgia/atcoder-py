import bisect
import itertools
import math


def main(case: str) -> None:
    NQ, As, *rest = [list(map(int, x.split())) for x in case.splitlines()]

    N, Q = NQ

    s_cnt = 0

    for query in rest:
        if query[0] == 1:
            (As[(query[1] - 1) - s_cnt], As[(query[2] - 1) - s_cnt]) = (
                As[(query[2] - 1) - s_cnt],
                As[(query[1] - 1) - s_cnt],
            )
            continue

        if query[0] == 2:
            s_cnt += 1

            if s_cnt == int(N):
                s_cnt = 0
            continue

        print(As[(query[1] - 1) - s_cnt])

        continue


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
8 5
6 17 2 4 17 19 1 7
2 0 0
1 7 2
1 2 6
1 4 5
3 4 0
        """,
        """
9 6
16 7 10 2 9 18 15 20 5
2 0 0
1 1 4
2 0 0
1 8 5
2 0 0
3 6 0
        """,
        """
11 18
23 92 85 34 21 63 12 9 81 44 96
3 10 0
3 5 0
1 3 4
2 0 0
1 4 11
3 11 0
1 3 5
2 0 0
2 0 0
3 9 0
2 0 0
3 6 0
3 10 0
1 6 11
2 0 0
3 10 0
3 4 0
3 5 0
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

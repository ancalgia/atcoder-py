import bisect
import itertools
import math

magic_num = 10**9 + 7


def main(case: str) -> None:
    NQ, As, *Upshifts = [list(map(int, x.split())) for x in case.splitlines()]

    N, Q = NQ

    # calced_As = [sum(x) for x in As]

    # matrix = [[0] * N] * Q
    matrix = [[0 for _ in range(N)] for _x in range(Q)]

    for i1, us in enumerate(Upshifts):
        for i2 in range(us[0] - 1, us[1]):
            matrix[i1][i2] += us[2]

    pass

    all_position_matrix = [As] + matrix

    all_fuben_matrix = [[0 for _ in range(N - 1)] for _x in range(Q + 1)]

    current_pos = 0

    for hogedex, hoge in enumerate(all_position_matrix):
        pass

        for fugadex, fuga in enumerate(hoge):
            if fugadex == 0:
                current_pos = fuga

            else:
                all_fuben_matrix[hogedex][fugadex - 1] = fuga - current_pos
                current_pos = fuga

    pass

    current_fuben = []

    for afdex, af in enumerate(all_fuben_matrix):
        pass
        if afdex == 0:
            current_fuben = af.copy()

        else:
            for curdex, curr in enumerate(current_fuben):
                curr += af[curdex]

            print(sum(map(abs, *current_fuben)))

    # for fugadex, x in enumerate(As):
    #     current_pos = 0

    #     current_fubens[fugadex] = x

    # print(all_scores)


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
3 3
1 2 3
2 3 1
1 2 -1
1 3 2
        """,
        """
20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7
            """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

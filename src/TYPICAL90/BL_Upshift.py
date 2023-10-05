import bisect
import itertools
import math

magic_num = 10**9 + 7


def main(case: str) -> None:
    NQ, As, *Upshifts = [list(map(int, x.split())) for x in case.splitlines()]

    N, Q = NQ

    outputs: list[int] = []

    curr_position = As

    # スライドさせてまとめて計算
    curr_fuben: list[int] = [r - l for l, r in zip(curr_position, curr_position[1:])]

    curr_total_fuben = sum([abs(x) for x in curr_fuben])

    for upshift in Upshifts:
        l_diff = 0
        r_diff = 0

        if upshift[0] != 1:
            tgt = curr_fuben[upshift[0] - 2]

            l_diff = abs(tgt + upshift[2]) - abs(tgt)

            curr_fuben[upshift[0] - 2] += upshift[2]

        if upshift[1] != N:
            tgt = curr_fuben[upshift[1] - 1]

            r_diff = abs(tgt - upshift[2]) - abs(tgt)

            curr_fuben[upshift[1] - 1] -= upshift[2]

        curr_total_fuben += l_diff + r_diff

        outputs.append(curr_total_fuben)

    [print(x) for x in outputs]


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

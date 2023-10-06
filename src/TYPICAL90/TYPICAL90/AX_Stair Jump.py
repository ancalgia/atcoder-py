import bisect
import itertools
import math


def main(case: str) -> None:
    N, L = list(map(int, case.split()))

    max_jump = N // L

    pattern_count = 0

    for x in range(max_jump + 1):
        single_steps = N - L * x

        moves = single_steps + x

        pattern_count += math.comb(moves, single_steps)

    magic_num = 10**9 + 7

    print(pattern_count if pattern_count < magic_num else pattern_count % magic_num)


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
3 2        
        """,
        """
4 4
        """,
        """
5 2
        """,
        """
6783 125
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

import bisect
import itertools
import math


def main(case: str) -> None:
    NL, K, A = case.splitlines()

    N, L = map(int, NL.split())

    K = int(K)

    AList = list(map(int, A.split()))

    whole_yokan = [0, *AList, L]

    whole_yokan_diffs = [r - l for l, r in zip(whole_yokan, whole_yokan[1:])]

    current_score = 1000000

    current_yokan = whole_yokan

    current_yokan_diffs = whole_yokan_diffs

    pass

    for x in range(K):
        pass

        for cut in range(len(current_yokan)):
            if cut == 0:
                continue
            if cut == len(current_yokan):
                continue

            left_yokan = current_yokan[:cut]
            right_yokan = current_yokan[cut:]

            left_length = sum(left_yokan)
            right_length = sum(right_yokan)

            # tmp_score =


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
3 34
1
8 13 26
        """,
        """
7 45
2
7 11 16 20 28 34 38
        """,
        """
3 100
1
28 54 81
        """,
        """
3 100
2
28 54 81
        """,
        """
20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

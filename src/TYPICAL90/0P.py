import bisect
import itertools
import math


def main(case: str) -> None:
    N, ABC = case.splitlines()

    tgt = int(N)

    A, B, C = map(int, ABC.split())

    MIN, MID, MAX = sorted([A, B, C])

    least_count = math.ceil(tgt // MAX)

    while True:
        for MAX_cnt in reversed(range(least_count + 1)):
            MAXsum = MAX_cnt * MAX

            if MAXsum > tgt:
                continue

            for MID_cnt in reversed(range(least_count - MAX_cnt + 1)):
                MIN_cnt = least_count - (MAX_cnt + MID_cnt)

                MIDsum = MID_cnt * MID

                MINsum = MIN_cnt * MIN

                if MAXsum + MIDsum > tgt:
                    continue

                if MAXsum + MIDsum + MINsum < tgt:
                    break

                if (MAXsum + MIDsum + MINsum) == tgt:
                    print(least_count)
                    return

        least_count += 1


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
972046963
945667046 972046963 3805433
        """,
        """
9999
1 5 10
        """,
        """
998244353
314159 265358 97932
        """,
        """
100000000
10001 10002 10003
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

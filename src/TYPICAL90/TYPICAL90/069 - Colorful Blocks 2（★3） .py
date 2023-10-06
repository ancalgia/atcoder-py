import bisect
import itertools
import math

magic_num = 10**9 + 7


def main(case: str) -> None:
    N, K = list(map(int, case.split()))

    if N == 1:
        print(K % magic_num)
        return

    elif N == 2:
        if K == 1:
            print(0)
            return
        else:
            print((K * (K - 1)) % magic_num)
            return

    else:
        if K < 3:
            print(0)
            return
        else:
            print((K * (K - 1) * pow(K - 2, N - 2, magic_num)) % magic_num)
            return


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
2 3
        """,
        """
10 2
        """,
        """
2021 617
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

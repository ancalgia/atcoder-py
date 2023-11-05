import itertools
import math


def main(case: str) -> None:
    (N, K, Q), As, Ls = [list(map(int, x.split())) for x in case.splitlines()]

    for x in Ls:
        if As[x - 1] == N:
            continue
        if As[x - 1] + 1 in As:
            continue

        As[x - 1] += 1

    print(" ".join(map(str, As)))


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
5 3 5
1 3 4
3 3 1 1 2
        """,
        """
2 2 2
1 2
1 2
        """,
        """
10 6 9
1 3 5 7 8 9
1 2 3 4 5 6 5 6 2
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

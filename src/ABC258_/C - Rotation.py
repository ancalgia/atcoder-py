import collections
import itertools


def main(case: str) -> None:
    NQ, S, *rest = case.splitlines()

    N, Q = list(map(int, NQ.split()))

    queries = [list(map(int, x.split())) for x in rest]

    SS = S + S

    indicator = N

    for x in queries:
        if x[0] == 1:
            indicator -= x[1]
        else:
            while indicator < N:
                indicator += N

            indicator -= N

            print(SS[indicator + x[1] - 1])


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
abc
2 2
1 1
2 2
        """,
        """
10 8
dsuccxulnl
2 4
2 7
1 2
2 7
1 1
1 2
1 3
2 5
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)

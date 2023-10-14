import collections
import itertools


def main(case: str) -> None:
    N, X, Y = list(map(int, case.split()))

    matrix: list[list[int]] = [[1 if x == 0 else 0, 0] for x in range(N)]

    for idx in range(N - 1):
        matrix[idx + 1][0] += matrix[idx][0]

        matrix[idx][1] += matrix[idx][0] * X

        matrix[idx + 1][0] += matrix[idx][1]

        matrix[idx + 1][1] += matrix[idx][1] * Y

    print(matrix[-1][-1])


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
2 3 4
        """,
        """
1 5 5
        """,
        """
10 5 5
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)

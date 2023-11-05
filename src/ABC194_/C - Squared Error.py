import collections
import itertools


def main(case: str) -> None:
    (N,), As = [list(map(int, x.split())) for x in case.splitlines()]

    existCounter = collections.Counter(As).most_common()

    result = 0

    for c1 in existCounter:
        for c2 in existCounter:
            result += ((c1[0] - c2[0]) ** 2) * c1[1] * c2[1]

    print(result // 2)


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
3
2 8 4 4 4 4 
        """,
        """
5
-5 8 9 -4 -3
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)

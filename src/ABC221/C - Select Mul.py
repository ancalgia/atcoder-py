import itertools


def main(case: str) -> None:
    N = case

    sortedNums = sorted([*N], reverse=True)

    left: list[str] = []
    right: list[str] = []

    for idx, x in enumerate(sortedNums):
        if idx == 0:
            left.append(x)
            continue

        if len(left) < len(right):
            left.append(x)
            continue
        elif len(left) > len(right):
            right.append(x)
            continue

        else:
            if left > right:
                right.append(x)
                continue
            else:
                left.append(x)
                continue

    leftNum = int("".join(left))
    rightNum = int("".join(right))

    print(leftNum * rightNum)


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
123
        """,
        """
1121
        """,
        """
998244353
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)

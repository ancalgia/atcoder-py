import bisect
import itertools
import math


def main(case: str) -> None:
    N, *rest = [list(map(int, x.split())) for x in case.splitlines()]

    A_runners = rest[: N[0]]

    M = rest[N[0]]

    X_rumors = rest[N[0] + 1 :]

    # 可能な順番を書き出す
    all_patterns = list(itertools.permutations(range(N[0]), N[0]))
    rumor_string = set(
        sum([["-" + str(x[0]) + "-" + str(x[1]) + "-", "-" + str(x[1]) + "-" + str(x[0]) + "-"] for x in X_rumors], [])
    )

    possible_patterns: list[tuple[int, ...]] = []
    for pattern in all_patterns:
        pattern_str = "-" + "-".join([str(y + 1) for y in pattern]) + "-"

        is_valid = True
        for rumor in rumor_string:
            if rumor in pattern_str:
                is_valid = False
                break

        if is_valid:
            possible_patterns.append(pattern)

    if len(possible_patterns) == 0:
        print("-1")
        return

    # 各パターンの所要時間を計算
    shortest = 10000000

    for pattern in possible_patterns:
        time = sum([A_runners[y][idx] for idx, y in enumerate(pattern)])

        shortest = min([time, shortest])

    print(shortest)


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
5
619 223 187 587 473
672 93 57 128 441
633 61 518 260 921
942 630 501 963 949
16 823 770 32 814
2
1 5
3 4
        """,  # 1341
        """
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2
1 3
2 3
        """,
        """
3
1 10 100
10 1 100
100 10 1
0
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

import bisect
import itertools


def main(case: str) -> None:
    (N, M, D), As, Bs = [list(map(int, x.split())) for x in case.splitlines()]

    # revAsSet = sorted(list(set(As)), reverse=True)
    # revBsSet = sorted(list(set(Bs)), reverse=True)

    revAsSet = sorted(list(set(As)))
    revBsSet = sorted(list(set(Bs)))

    tmp = 0

    for a in revAsSet:
        # if revBsSet[0] + D < a:
        #     continue

        # if revBsSet[-1] - D > a:
        #     break

        # if a + a + D <= tmp:
        #     break

        # tgt = next((x for x in revBsSet if a - D <= x <= a + D), None)
        tgt = bisect.bisect_right(revBsSet, a + D)

        if a - D <= revBsSet[tgt - 1] <= a + D:
            tmp = max(tmp, a + revBsSet[tgt - 1])

    if tmp == 0:
        print(-1)
        return

    print(tmp)


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
2 3 2
3 10
2 5 15
        """,
        """
3 3 0
1 3 3
6 2 7
        """,
        """
1 1 1000000000000000000
1000000000000000000
1000000000000000000
        """,
        """
8 6 1
2 5 6 5 2 1 7 9
7 2 5 5 2 4
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

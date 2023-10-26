import itertools


def main(case: str) -> None:
    N, As = case.splitlines()

    N = int(N)

    bricks = list(map(int, As.split()))

    if 1 not in bricks:
        print(-1)
        return

    startidx = 0
    lastidx = 0

    expected_next_brick = 1

    for idx, x in enumerate(bricks):
        if x != expected_next_brick:
            continue

        else:
            if expected_next_brick == 1:
                startidx = idx
                lastidx = idx
            else:
                lastidx = idx

            expected_next_brick += 1

    # print(N - (lastidx - startidx) + expected_next_brick)
    print((startidx) + (N - (lastidx + 1)) + (lastidx - (startidx - 1) - (expected_next_brick - 1)))


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
2 1 2
        """,
        """
3
2 2 2
        """,
        """
10
3 1 4 1 5 9 2 6 5 3
        """,
        """
1
1
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

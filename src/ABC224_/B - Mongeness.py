import itertools
import math


def main(case: str) -> None:
    (H, W), *matrix = [list(map(int, x.split())) for x in case.splitlines()]

    ng_count = 0

    for h_idx in range(H):
        if h_idx + 1 == H:
            continue

        pass
        for w_idx in range(h_idx, W):
            if w_idx + 1 == W:
                continue

    print("YES" if ng_count == 0 or ng_count == 2 else "NO")


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
2 1 4
3 1 3
6 4 1
        """,
        """
2 4
4 3 2 1
5 6 7 8
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

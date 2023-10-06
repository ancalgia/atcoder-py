import bisect
import itertools
import math

magic_num = 10**9 + 7


def main(case: str) -> None:
    N, cakes = [list(map(int, x.split())) for x in case.splitlines()]

    all_cake = sum(cakes)

    if all_cake % 10 != 0:
        # 合計が10の倍数でなければ絶対にNo
        print("No")
        return

    tgt_size = sum(cakes) // 10

    # ケーキを二つ繋げとく
    two_cakes = cakes + cakes

    left = 0
    right = 0

    curr_size = 0

    # 尺取り法
    while True:
        if curr_size == tgt_size:
            print("Yes")
            return

        if curr_size < tgt_size:
            if right >= len(two_cakes) - 1:
                print("No")
                return

            curr_size += two_cakes[right]
            right += 1
        else:
            curr_size -= two_cakes[left]
            left += 1


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
10
1 1 1 1 1 1 1 1 1 1
        """,
        """
3
1 1 1
        """,
        """
3
1 18 1
        """,
        """
4
1 9 1 9
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

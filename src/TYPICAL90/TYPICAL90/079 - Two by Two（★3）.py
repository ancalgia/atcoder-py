import bisect
import itertools
import math

magic_num = 10**9 + 7


def main(case: str) -> None:
    HW, *matrix2 = [list(map(int, x.split())) for x in case.splitlines()]

    H, W = HW

    matrix_from = matrix2[:H].copy()
    matrix_to = matrix2[H:].copy()

    diff = abs(sum([sum(x) for x in matrix_from]) - sum([sum(x) for x in matrix_to]))

    if diff % 4 != 0:
        # 差が4の倍数でなけばクリア不可（自明）
        print("No")
        return

    tgt_matrix: list[list[int]] = []

    for h_idx in range(H):
        tgt_row: list[int] = []

        for w_idx in range(W):
            tgt_row.append(matrix_to[h_idx][w_idx] - matrix_from[h_idx][w_idx])

        tgt_matrix.append(tgt_row)

    pass

    counter = 0

    for h_idx in range(H):
        for w_idx in range(W):
            # 最終列or 最終列の場合は判定のみ行い、ズレてれば終了
            if w_idx == W - 1 or h_idx == H - 1:
                if tgt_matrix[h_idx][w_idx] != 0:
                    print("No")
                    return
                else:
                    continue

            diff = tgt_matrix[h_idx][w_idx]
            if diff == 0:
                continue

            tgt_matrix[h_idx][w_idx] -= diff
            tgt_matrix[h_idx + 1][w_idx] -= diff
            tgt_matrix[h_idx][w_idx + 1] -= diff
            tgt_matrix[h_idx + 1][w_idx + 1] -= diff
            counter += abs(diff)

    print("Yes")
    print(counter)


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
0 0 0
0 0 0
0 0 0
1 1 0
1 1 0
0 0 0
        """,
        """
3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 1 0
0 0 0
        """,
        """
5 5
6 17 18 29 22
39 50 25 39 25
34 34 8 25 17
28 48 25 47 42
27 47 24 32 28
4 6 3 29 28
48 50 21 48 29
44 44 19 47 28
4 49 46 29 28
4 49 45 1 1
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

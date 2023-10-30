import itertools
from typing import Literal


def main(case: str) -> None:
    (N, Q), *Es = [list(map(int, x.split())) for x in case.splitlines()]

    ppl_stats_list: list[Literal["UNCALLED", "CALLED", "VISITED"]] = ["UNCALLED" for x in range(N)]

    last_called_man = 0

    filteredEs = filter(lambda x: x[0] != 1, Es)

    for x in filteredEs:
        if x[0] == 2:
            ppl_stats_list[x[1] - 1] = "VISITED"
        elif x[0] == 3:
            tgt_idx = ppl_stats_list.index("UNCALLED", last_called_man)

            print(tgt_idx + 1)
            last_called_man = tgt_idx


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
4 10
1
1
3
2 1
1
2 3
3
1
2 2
3
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

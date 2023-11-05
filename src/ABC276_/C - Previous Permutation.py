import itertools
from typing import Literal


def main(case: str) -> None:
    (N,), Ps = [list(map(int, x.split())) for x in case.splitlines()]

    reversedPs = list(reversed(Ps))

    tgtidx = 99999
    current_num = 0
    for idx, x in enumerate(reversedPs):
        if idx == 0:
            current_num = x
            continue

        else:
            if current_num < x:
                tgtidx = idx
                break
            else:
                current_num = x
                continue

    changenum1st = max([x for x in reversedPs[:tgtidx] if x < reversedPs[tgtidx]])
    changeidx1st = reversedPs.index(changenum1st)

    (reversedPs[tgtidx], reversedPs[changeidx1st]) = (reversedPs[changeidx1st], reversedPs[tgtidx])

    restSorted = sorted(reversedPs[:tgtidx])

    result = restSorted + reversedPs[tgtidx:]

    result.reverse()

    print(*result)


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
3 1 2
        """,
        """
10
9 8 6 5 10 3 1 2 4 7
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

import itertools
from typing import Literal


def main(case: str) -> None:
    (N, M), *rest = [list(map(int, x.split())) for x in case.splitlines()]

    As = [x for idx, x in enumerate(rest) if idx % 2 == 1]

    allSet = [list(itertools.combinations(As, x)) for x in range(1, M + 1)]

    flat1Set = itertools.chain.from_iterable(allSet)

    flat2Set = [list(set(itertools.chain.from_iterable(x))) for x in flat1Set]

    lenSet = [len(x) for x in flat2Set]

    print(lenSet.count(N))


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
1 4
1
1
1
1
1
1
1
1
        """,
        """
4 2
2
1 2
2
1 3
        """,
        """
6 6
3
2 3 6
3
2 4 6
2
3 6
3
1 5 6
3
1 3 6
2
1 4
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

import bisect
import itertools
import math


def main(case: str) -> None:
    N, As, Bs, Cs = [list(map(int, x.split())) for x in case.splitlines()]

    modAs, modBs, modCs = [
        [x % 46 for x in As],
        [x % 46 for x in Bs],
        [x % 46 for x in Cs],
    ]

    all_patterns = list(itertools.product(modAs, modBs, modCs))

    counter = 0
    for p in all_patterns:
        s = sum(p)

        if s != 0 and s != 46 and s != 92 and s != 138:
            continue

        counter += 1

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
3
10 13 93
5 27 35
55 28 52
        """,
        """
3
10 56 102
16 62 108
20 66 112
        """,
        """
20
238 395 46 238 264 114 354 52 324 14 472 64 307 280 209 24 165 194 179 248
270 83 377 332 173 21 362 75 66 342 229 117 124 481 48 235 376 13 420 74
175 427 76 278 486 169 311 47 348 225 41 482 355 356 263 95 170 156 340 289
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)

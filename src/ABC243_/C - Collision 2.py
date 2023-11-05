import collections
import itertools


def main(case: str) -> None:
    N, *S = case.splitlines()

    persons = [list(map(int, x.split())) for x in S[:-1]]

    personsWithDirectionSet = set([(x[0], x[1], d) for x, d in zip(persons, S[-1])])

    personAxisYList = [x[1] for x in personsWithDirectionSet]

    AxisYCounter = collections.Counter(personAxisYList).most_common()

    mustCheckAxisY = set([x[0] for x in AxisYCounter if x[1] >= 2])

    pass

    for y in mustCheckAxisY:
        tgt = set(filter(lambda x: x[1] == y, personsWithDirectionSet))

        rights = set(filter(lambda x: x[2] == "R", tgt))
        lefts = set(filter(lambda x: x[2] == "L", tgt))

        if len(rights) == 0 or len(lefts) == 0:
            continue

        minRight = min(filter(lambda x: x[2] == "R", tgt))
        maxLeft = max(filter(lambda x: x[2] == "L", tgt))

        if minRight <= maxLeft:
            print("Yes")
            return

    print("No")


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
2 3
1 1
4 1
RRL
        """,
        """
2
1 1
2 1
RR
        """,
        """
10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)

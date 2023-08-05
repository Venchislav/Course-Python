import itertools


def main() -> None:
    items = '123'
    items2 = '456'
    print(list(itertools.chain(items, items2)))
    # MORE!!!
    print(list(itertools.combinations(itertools.chain(items, items2), 3)))
    # MORE!!!!!!
    print(list(itertools.combinations(itertools.chain(items, items2), len(list(itertools.chain(items, items2))) // 2)))
    # but it's freakin unreadable and hard to understand (line 11)

    print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(1, 11))))
    # similar to:
    print(list(filter(lambda x: x % 2 == 1, range(1, 11))))

    # works until function returns false
    print(list(itertools.takewhile(lambda x: x % 2 == 0, range(0, 11))))

    # starmap looks familiar to map

    print(list(itertools.starmap(lambda x, y: x * y, [(1, 2), (2, 3), (3, 4)])))


if __name__ == '__main__':
    main()

import itertools


def perms_tools(iterable):
    perms = itertools.permutations(iterable)
    for perm in perms:
        print(perm)

    print('---------\nperms2', end='\n-------\n')

    # 2nd arg is len of our permutation
    perms2 = itertools.permutations(iterable, 2)
    for perm in perms2:
        print(perm)

    print('---------\ncombinations', end='\n-------\n')

    # if we want to get combinations

    combs = itertools.combinations(iterable, 2)
    for comb in combs:
        print(comb)

    print('---------\ncombinations-replacement', end='\n-------\n')

    # if we want to get combinations with replacement

    combs2 = itertools.combinations_with_replacement(iterable, len(iterable))
    for comb in combs2:
        print(comb)

    # easier way to print it

    print(list(itertools.combinations_with_replacement(iterable, len(iterable))))


if __name__ == '__main__':
    perms_tools(['1', '2', '3'])

import itertools


def main() -> None:
    # starts counting loop from arg value
    for i in itertools.count(10):
        print(i)
        if i == 15:
            break

    print('---------\nrepeating', end='\n-------\n')

    # repeats arg1 arg2 times
    for i in itertools.repeat(10, 4):
        print(i)

    print('---------\naccumulating', end='\n-------\n')

    # repeats arg1 arg2 times
    for i in itertools.accumulate(range(1, 11)):
        print(i)


if __name__ == '__main__':
    main()

def main():
    countries = ('Ger', 'Eng', 'UA')
    country_iter = iter(countries)

    while True:
        try:
            print(next(country_iter))
        except StopIteration:
            print('End of iterable')
            break


# code above is the same to:

for i in ('Ger', 'Eng', 'UA'):
    print(i)

print('--------')

if __name__ == '__main__':
    main()

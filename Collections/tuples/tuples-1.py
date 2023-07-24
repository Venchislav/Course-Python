person = ('John', 'Doe', 'May', 12, 1997)

name, birthday = person[:2], person[2:]
print(name)

# or named slices to make code more readable(but actually not really)

NAME, BIRTHDAY = slice(2), slice(2, None)
print(person[NAME])

# reversed is longer and harder to understand, but it doesn't make copy of iterable(slices do)
print(tuple(reversed(person[NAME])))
print(person[NAME][::-1])
print(list(reversed(range(100))))
# we can even reverse range like this:
# start end step
print(list(range(10, -1, -1)))
# but that's a dumb way
print(list(reversed(range(10 + 1))))

# and just for the fact and for understanding: tuple behaves like str (mostly)

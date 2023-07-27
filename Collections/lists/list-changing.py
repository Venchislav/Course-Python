xs = [1, 2, 3, 4, 5, 6]

print(list(reversed(xs)))

print(xs.reverse())  # None
print(xs)  # it reverses it inplace with no output at very beginning

# the same thing is about sort and sorted

print(xs.sort())
print(sorted(xs))

xs = [1, 2, 3]
xs.append(42)
xs.extend({-1, -2})  # = for item in {-1, -2}: xs.append(item)
print(xs)

xs = [1, 2, 3]
# insert item before indexed elem
# before elem with index 0
xs.insert(0, 4)
print(xs)  # [4, 1, 2, 3]
# before elem with index 3
xs.insert(3, 23)
print(xs)  # [4, 1, 2, 23, 3]

# this also works

xs = [1, 2, 3]
xs[:2] = [0] * 2  # [0, 0, 3]
print(xs)

xs, ys = [1, 2, 3], [4, 5, 6]
xs += ys
print(xs)  # [1, 2, 3, 4, 5, 6]
# works as extend


xs = []


def f():
    global xs
    xs += [42]
    return xs


print(f())
# it won't work without xs as it makes local version of this var in func
# but code below with append will
xs = []


def f():
    xs.append(42)
    return xs


print(f())


# sadly this sh*t below works:

xs = []
xs += 'abcdef'
print(xs)

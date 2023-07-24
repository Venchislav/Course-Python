from collections import namedtuple

# Person is a class name, list is a list of tuple items
Person = namedtuple("Person", ["name", "age"])

p = Person('John', age=77)
print(p._fields)
print(p.name, p.age)

# makes dict from our tuple
print(p._asdict())
# replace elem in our namedtuple
# and it's magic
p = p._replace(name='Jane')
print(p)

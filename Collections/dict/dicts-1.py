d = dict(name='John', lastname='Doe')
print(d)

# dict constructor is better as we don't have to use '' with str keys, we just write it as kwargs
# creates dict with default None vals (or with 2nd arg vals)
print(dict.fromkeys(['foo', 'bar']))
print(dict.fromkeys(['foo', 'bar'], 6))

print(d.keys())
print(d.items())
print(d.values())

# iter like this
print({v for v in d.values()})
# or
# set as keys are close to set(they don't repeat)
for k in set(d):
    del d[k]
print(d)

d = dict(foo='bar')

# print(d["boo"])  # err as we don't have boo

# so in this case we can use get
# if we have an item we get it, if we don't we return a message or a value
print(d.get("boo", "There's no boo in dict"))  # There's no boo in dict
print(d.get("foo", "There's no foo in dict"))  # bar
# it's None value on default

d = dict(foo='bar')

d.setdefault('boo', '???')
print(d)  # {'foo': 'bar', 'boo': '???'}


d.setdefault('foo', '???')
print(d)  # {'foo': 'bar', 'boo': '???'}

# these methods are useful

from collections import Counter

c = Counter(['foo', 'foo', 'foo', 'bar'])
# c['foo'] += 1
print(c)

# Count counts all hashable elems

print(c['foo'])

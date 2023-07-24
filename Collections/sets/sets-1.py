seen = set()
seen.add(42)
print(seen)

seen.update([1, 2])
print(seen)
seen.update([], [1, 3], [4, 5])
print(seen)

# remove vs discard

seen.remove(42)  # it works, but if we don't have this elem it will cause en error

# so we can use discard

seen.discard(42)  # works only if we have this elem (here it passes as we've already removed 42)
print(seen)

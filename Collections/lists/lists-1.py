# matrix creation in this way looks great, but...
print([[0] * 3] * 2)

chunks = [[0] * 3] * 3
print(chunks)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
chunks[0][0] = 1
print(chunks)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
# and yeah... awful result

print('-------------')
# good solution

chunks2 = [[0 for _ in range(3)] for _ in range(3)]
print(chunks2)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
chunks2[0][0] = 1
print(chunks2)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

# it works as we don't make copies of links objects

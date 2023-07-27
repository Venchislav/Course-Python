from collections import deque

q = deque([1, 2, 3])
# appends elem on left
q.appendleft(0)
print(q)

q.append(4)
print(q)

# pops left elem of the list
q.popleft()
print(q)

# deque was used in BFS algorithm

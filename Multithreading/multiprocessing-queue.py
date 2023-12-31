from multiprocessing import Queue


colors = ['red', 'green', 'blue', 'black']
cnt = 1
queue = Queue()
print('pushing items to queue:')
for color in colors:
    print(f'item no: {cnt} {color}')
    queue.put(color)
    cnt += 1

print('\npopping items from queue:')
cnt = 0

while not queue.empty():
    print('item no: ', cnt, ' ', queue.get())
    cnt += 1

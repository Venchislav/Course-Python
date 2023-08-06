import time
import threading

stop = False


def counter():
    cnt = 0
    while not stop:
        time.sleep(1)
        cnt += 1
        print(cnt)


# calls our function in thread
threading.Thread(target=counter).start()

# works in another thread
input('Press enter to stop counter\n')
stop = True

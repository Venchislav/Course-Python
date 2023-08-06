import time
import threading


def counter(desc):
    cnt = 0
    while True:
        time.sleep(1)
        cnt += 1
        print(f'{desc}: {cnt}')


# just calls func with args
threading.Thread(target=counter, daemon=True, args=('Hello world!',)).start()
threading.Thread(target=counter, daemon=True, args=('Bye world!',)).start()

# and don't forget that args is tuple so , is required

input('Press Enter to quit counter\n')

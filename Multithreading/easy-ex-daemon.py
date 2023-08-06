import time
import threading


def counter():
    cnt = 0
    while True:
        time.sleep(1)
        cnt += 1
        print(cnt)


threading.Thread(target=counter, daemon=True).start()

# we don't have done var here, but counter will be stopped
# as daemon thread is not important, and we stop it as important process was finished
input('Press Enter to quit counter\n')


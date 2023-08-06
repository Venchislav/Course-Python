import multiprocessing
import math


def calc():
    for i in range(70000000):
        math.sqrt(i)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    for i in range(10):
        multiprocessing.Process(target=calc).start()

import threading
import time

from datetime import datetime


def open_pack():
    time.sleep(5)


def put_in_plate():
    time.sleep(3)


def boil_water():
    time.sleep(15)


def wait(t: int):
    time.sleep(t)


start = datetime.now()
open_pack()
put_in_plate()
boil_water()
wait(10)
wait(20)
print(datetime.now() - start)


start1 = datetime.now()
threading.Thread(target=boil_water).start()
open_pack()
put_in_plate()
wait(10)
wait(20)
print(datetime.now() - start1)

import time


# our outer decorator function
def measure_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        try:
            # we try to return result of execution of our decorated func
            return func(*args, **kwargs)
        # and finally(even if try didn't work) we print execution time
        finally:
            ex_time = time.time() - start_time
            print(f'Execution time: {ex_time:.3f} seconds')

    return inner


def url(url):
    time.sleep(1)
    return url + ' Hello world!'


url = measure_time(url)
print(url('python.org'))

# url function execution before decorating:

# sleep time -> return url and hello world

# url function execution after decorating:

# start_time = time.time() -> sleep time -> return url and hello world -> ex_time -> print(ex_time)

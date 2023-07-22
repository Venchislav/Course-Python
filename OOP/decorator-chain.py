import time


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


def memoize(func):
    _cache = {}

    def wrapper(*args, **kwargs):
        name = func.__name__
        key = (name, args, frozenset(kwargs.items()))
        if key in _cache:
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result

    return wrapper


def url(url):
    time.sleep(1)
    return url + ' Hello world!'


url = measure_time(memoize(url))
print(url('python.org'))

# but there's an easier way to decorate functions with @ symbol
# decorators chain is read from bottom to top


@memoize
@measure_time
def url(url):
    time.sleep(1)
    return url + ' Hello world!'

print(url('python.org'))

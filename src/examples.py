import functools


class cache:
    def __init__(self, ttl: int):
        self._ttl = ttl
        self.__results = {}

    def __call__(self, func, *args, **kwargs):
        @functools.wraps(func)
        def wrapper(*args):
            if args in self.__results:
                print('cached value')
                return self.__results[args]

            print('calculated')
            self.__results[args] = func(*args)
            return self.__results[args]

        return wrapper


def my_cache(ttl):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            return fun(*args, **kwargs)
        return wrapper
    return decorator


# @cache(ttl=40)
def foo(a, b):
    #
    return a * b


if __name__ == '__main__':
    foo(2,2)
    foo(2,3)
    foo(2,2)
    foo(2,5)
    foo(2,2)

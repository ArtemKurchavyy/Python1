def val_checker(f):
    def _val_checker(func):
        def wrapper(x):
            if f(x) is True:
                return func(x)
            else:
                raise ValueError(f'wrong val: {x}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)

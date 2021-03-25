def type_logger(func):
    def wrapper(*args):
        a = ', '.join([f'{func.__name__}({arg}: {type(arg)})' for arg in args])
        return a

    return wrapper


@type_logger
def calc_cube(*args):
    a = ', '.join([f'{arg ** 3}' for arg in args])
    return a


c = calc_cube(5, 6, 10)
print(c)

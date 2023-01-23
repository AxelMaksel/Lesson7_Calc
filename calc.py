import excepts as ex

def input_2_num():
    return input("ВВедите два числа через пробел: ")


def sum(x, y):
    return f'res = {x + y}'


def sum(x, y):
    return (x + y)


def sub(x, y):
    return (x - y)


def mul(x, y):
    return (x * y)


def div01(x, y):
    if ex.check_zero(x, y):
        return (float(x) / float(y))


def div02(a, b):
    return (a // b)


def div03(a, b):
    return (a % b)


def pow(a, b):
    return (a ** b)


def sqrt(a):
    return (a ** 0.5)

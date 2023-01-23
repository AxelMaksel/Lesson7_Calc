import excepts as ex
from logg import logging

def input_2_num():
    a, b = "", ""
    while not a and not b:
        print("ВВедите два числа через пробел: ")
        ls = input().split()
        if len(ls) == 2 and ls[0].isnumeric() and ls[1].isnumeric():
            a, b = ls
            logging.info(f'Input two numbers {a},{b}')
            return a,b
        else:
            logging.error(f'Input two numbers {ls}')
            


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
        r =float(x) / float(y)
        logging.info(f'Result {x}/{y}={r}')
        return (r)


def div02(a, b):
    return (a // b)


def div03(a, b):
    return (a % b)


def pow(a, b):
    return (a ** b)


def sqrt(a):
    return (a ** 0.5)

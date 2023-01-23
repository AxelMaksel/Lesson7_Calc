import excepts as ex
from logg import logging


def input_2_num():
    a, b = "", ""
    while not a and not b:
        print("ВВедите два числа через пробел: ")
        ls = input().split()
        # if len(ls) == 2 and ls[0].isnumeric() and ls[1].isnumeric():
        if len(ls) == 2 and float(ls[0]) and float(ls[1]):
            a, b = ls
            logging.info(f'Input two numbers {a},{b}')
            return a, b
        else:
            logging.error(f'Input two numbers {ls}')


def sum(x, y):
    r = float(x) + float(y)
    logging.info(f'Result {x}+{y}={r}')
    return (r)


def sub(x, y):
    r = float(x) - float(y)
    logging.info(f'Result {x}-{y}={r}')
    return (r)


def mul(x, y):
    r = float(x) * float(y)
    logging.info(f'Result {x}*{y}={r}')
    return (r)


def div01(x, y):
    if ex.check_zero(x, y):
        r = float(x) / float(y)
        logging.info(f'Result {x}/{y}={r}')
        return (r)


def div02(x, y):
    if ex.check_zero(x, y):
        r = float(x) // float(y)
        logging.info(f'Result {x}//{y}={r}')
        return (r)


def div03(x, y):
    if ex.check_zero(x, y):
        r = float(x) % float(y)
        logging.info(f'Result {x}%{y}={r}')
        return (r)


def pow(x, y):
    r = float(x) ** float(y)
    logging.info(f'Result {x}**{y}={r}')
    return (r)


def sqrt(a):
    return (a ** 0.5)

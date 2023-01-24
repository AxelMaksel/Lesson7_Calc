import excepts as ex
from logg import logging


def print_result(st,a):
    print(f"\033[31m*"*40)
    print(f"{st}{a}")
    print("*"*40, f"\033[0m")


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


def input_1_num():
    a = ""
    while not a:
        print("ВВедите числО: ")
        ls = input().split()
        if len(ls) == 1 and float(ls[0]):
            a = ls[0]
            logging.info(f'Input ОДНО numbers {a}')
            return a
        else:
            logging.error(f'Input one numbers {ls}')


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


def div_1(x, y):
    if ex.check_zero(x, y):
        r = float(x) / float(y)
        logging.info(f'Result {x}/{y}={r}')
        return (f"{round(r,5)}")


def div_2(x, y):
    if ex.check_zero(x, y):
        r = float(x) // float(y)
        logging.info(f'Result {x}//{y}={r}')
        return (f"{round(r,5)}")


def div_3(x, y):
    if ex.check_zero(x, y):
        r = float(x) % float(y)
        logging.info(f'Result {x}%{y}={r}')
        return (f"{round(r,5)}")


def pow(x, y):
    r = float(x) ** float(y)
    logging.info(f'Result {x}**{y}={r}')
    return (f"{round(r,5)}")


def sqrt(x):
    r = float(x) ** 0.5
    logging.info(f'Result {x}')
    return (f"{round(r,5)}")

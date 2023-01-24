import excepts as ex
from logg import logging


def print_result(st, a):
    print(f"\033[31m*"*40)
    print(f"{st}{a}")
    print("*"*40, f"\033[0m")


def input_2_num():
    a, b = "", ""
    while not a and not b:
        print("Введите два числа через пробел: ")
        ls = input().split()
        # if len(ls) == 2 and ls[0].isnumeric() and ls[1].isnumeric():
        if len(ls) == 2 and float(ls[0]) and float(ls[1]):
            a, b = ls
            logging.info(f'Input two numbers {a} , {b}')
            return a, b
        else:
            logging.error(f'Input two numbers {ls}')


def input_complex():
    print("Сначала вводим действительную и мнимую части первого числа:")
    a1, b1 = input_2_num()
    print("Теперь действительную и мнимую части второго числа:")
    a2, b2 = input_2_num()
    c1 = complex(float(a1), float(b1))
    c2 = complex(float(a2), float(b2))
    print(f"Вы ввели комплексные числа {c1} и {c2} ")
    logging.info((f'Input two complex {c1} , {c2}'))
    return c1, c2


def input_1_complex():
    print("Вводим действительную и мнимую части комлексного числа:")
    a1, b1 = input_2_num()
    c1 = complex(float(a1), float(b1))
    print(f"Вы ввели комплексное число {c1} ")
    logging.info((f'Input щту complex {c1}'))
    return c1


def input_1_num():
    a = ""
    while not a:
        print("Введите число: ")
        ls = input().split()
        if len(ls) == 1 and float(ls[0]):
            a = ls[0]
            logging.info(f'Input one numbers {a}')
            return a
        else:
            logging.error(f'Input one numbers {ls}')


def sum(x, y):
    r = float(x) + float(y)
    logging.info(f'Result {x}+{y}={r}')
    return (r)


def sum_compl(x, y):
    r = x + y
    logging.info(f'Result {x}+{y}={r}')
    return (r)


def sub(x, y):
    r = float(x) - float(y)
    logging.info(f'Result {x}-{y}={r}')
    return (r)


def sub_compl(x, y):
    r = x - y
    logging.info(f'Result {x}-{y}={r}')
    return (r)


def mul(x, y):
    r = float(x) * float(y)
    logging.info(f'Result {x}*{y}={r}')
    return (r)


def mul_compl(x, y):
    r = x * y
    logging.info(f'Result {x}*{y}={r}')
    return (r)


def div_1(x, y):
    if ex.check_zero(x, y):
        r = float(x) / float(y)
        logging.info(f'Result {x}/{y}={r}')
        return (f"{round(r,5)}")


def div_compl(x, y):
    r = x / y
    logging.info(f'Result {x}/{y}={r}')
    return (r)


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


def pow_compl(x, y):
    r = x ** float(y)
    logging.info(f'Result {x}**{y}={r}')
    return (r)


def sqrt(x):
    r = float(x) ** 0.5
    logging.info(f'Result {x}')
    return (f"{round(r,5)}")


def sqrt_compl(x):
    r = x ** 0.5
    logging.info(f'Result {x}**{0.5}={r}')
    return (r)

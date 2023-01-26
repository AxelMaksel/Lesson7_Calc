import excepts as ex
from logg import logging

def input_2_num():
    a, b = "", ""
    while not a and not b:
        print("Введите два числа через пробел: ")
        ls = input().split()
        if len(ls) == 2 and ex.validate((ls[0])) and ex.validate((ls[1])):
            a = float(ls[0])
            b = float(ls[1])
            logging.info(f'Input two numbers {a} , {b}')
            return (a,b)
        else:
            logging.error(f'Input no numbers {ls}')
        

def input_1_num():
    a = ""
    while not a:
        print("Введите одно число: ")
        ls = input().split()
        if len(ls) == 1 and ex.validate((ls[0])):
            a = float(ls[0])
            logging.info(f'Input one numbers {a}')
            return a
        else:
            logging.error(f'Input no numbers {ls}')

def sum(x, y):
    r = x + y
    logging.info(f'Result {x}+{y}={r}')
    return r

def sub(x, y):
    r = x - y
    logging.info(f'Result {x}-{y}={r}')
    return r

def mul(x, y):
    r = x * y
    logging.info(f'Result {x}*{y}={r}')
    return r

def div_1(x, y):
    if ex.check_zero(x,y):
        r = x / y
        logging.info(f'Result {x}/{y}={r}')
    else:
        logging.error('Tried to divide by zero')
        print ("Делить на ноль нельзя!")
        x,y = input_2_num()
        r = div_1(x,y)
    return r

def div_2(x, y):
    if ex.check_zero(x,y):
        r = float(x) // float(y)
        logging.info(f'Result {x}//{y}={r}')
    else:
        logging.error('Tried to divide by zero')
        print ("Делить на ноль нельзя!")
        x,y = input_2_num()
        r = div_2(x,y)
    return r

def div_3(x, y):
    if ex.check_zero(x,y):
        r = float(x) % float(y)
        logging.info(f'Result {x}//{y}={r}')
    else:
        logging.error('Tried to divide by zero')
        print ("Делить на ноль нельзя!")
        x,y = input_2_num()
        r = div_3(x,y)
    return r

def pow(x, y):
    r = x ** y
    logging.info(f'Result {x}**{y}={r}')
    return r

def sqrt(x):
    if ex.check_posit(x):
        r = float(x) ** 0.5
        logging.info(f'Result = {r}')
    else:
        logging.error(f'Tried to extract the square root of a negative number {x}')
        print ("Квадратный корень из отрицательного числа не извлекается!")
        x = input_1_num()
        r = sqrt(x)
    
    return r

def sqrt_complex(x):
    r = x ** 0.5
    logging.info(f'Result = {r}')

    return r

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
    logging.info((f'Input one complex {c1}'))
    return c1

def print_result(st, a):
    print(f"{st}{a}\n")

# x,y = input_complex()
# a = div_1(x,y)
# print(a)
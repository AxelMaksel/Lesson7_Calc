from logg import logging

def check_zero(x, y):
    logging.info('Check division by zero')
    if x.isnumeric() and y.isnumeric() and y != "0":
        return True
    return False


def check_num(x, y):
    logging.info('проверка на число')
    if x.isnumeric() and y.isnumeric():
        return True
    return False


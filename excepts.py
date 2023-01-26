import types
from logg import logging

def check_zero(x, y):
    try:
        x/y
        valid = True
    except Exception:
        logging.error('Tried to divide by zero')
        valid = False

    return valid

def validate(userInput):
    try:
        transf = float(userInput)
        valid = True
    except Exception:
        logging.error('tried to input a non-numeric value')
        valid = False

    return valid

def check_posit(x):
    logging.info('Checking for negativity')
    if x>=0:
        return True
    return False
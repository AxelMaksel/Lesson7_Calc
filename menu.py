import menu_comp as mc
import menu_rac as rc
from logg import logging

def menu():
    while True:

        num_type=input("С какими числами работаем?\n"
                      "1 - Комплексные\n"
                      "2 - Рациональные\n"
                      "3 - Выход\n")

        match num_type:
            case "1":
                logging.info('Interaction with complex numbers')
                mc.menu_comp()
            case "2":
                logging.info('Interaction with rational numbers')
                rc.menu_rac()
            case "3":
                logging.info('Interrupting work in the program')
                break
            case _:
                logging.info('Restarting the program')
                print("Вы выбрали неверное значение: уточните выбор или нажмите 3 для прекращения работы программы")